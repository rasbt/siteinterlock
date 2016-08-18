import os
import sys


class Pdb():
    """ Object that allows operations with protein files in PDB format. """

    def __init__(self):
        self.cont = []

    def read_pdbfile(self, file_path):
        with open(file_path, 'r') as pdb_file:
            self.cont = [row.strip() for row
                         in pdb_file.read().split('\n') if row.strip()]
        self._process_pdb()
        return self

    def _process_pdb(self):
        if self.cont:
            self.atom = [row for row in self.cont if row.startswith('ATOM')]
            self.atom_no_h = [row for row in self.atom if 'H' not
                              in row[11:17]]
            self.hetatm = [row for row in self.cont
                           if (row.startswith('HETATM') and
                               row[17:20] != 'XXX')]
            self.heavy_atom = [row for row in self.atom
                               if 'H' not in row[12:16]]
            self.heavy_hetatm = [row for row in self.hetatm
                                 if 'H' not in row[12:16]]
            self.mainchain = [row for row in self.atom if
                              row[13:15] in ('CA', 'N ', 'C ', 'O ')]
            self.calpha = [row for row in self.mainchain
                           if row[13:15] == 'CA']

    def get_bfactors(self, protein=True, ligand=False, atoms='all'):
        """
        Collects b-factors (temperature factors) from ATOM
        and/or HETATM entries in a list.

        Parameters
        ----------
        protein : `bool`.
          If `True`, includes ATOM entries in calculation.

        ligand : `bool`.
          If `True`, includes HETATM entries in calculation.

        atoms : `str` (default: `'all'`)
          A string `'all'`, `'mainchain'`, `'calpha'`
          `"all"`: Includes all atoms in the RMSD calculation.
          `"mainchain"`: Only considers protein mainchain atoms (N, CA, O, C).
          `"calpha"`: Only considers C-alpha protein atoms.
          `"heavy"`: Only considers all atoms but hydrogen.

        Returns
        ----------
        bfactors : `list`
          B-factors as floats in a list.

        """
        if atoms not in ('all', 'mainchain', 'calpha', 'heavy'):
            raise ValueError('Invalid argument. '
                             'Argument not in ("all", '
                             '"mainchain", "calpha", "heavy"')

        bfactors = []
        if atoms == 'mainchain':
            bfactors += [float(line[60:66].strip()) for line in self.mainchain]
        elif atoms == 'calpha':
            bfactors += [float(line[60:66].strip()) for line in self.calpha]
        elif atoms == 'heavy':
            if protein:
                bfactors += [float(line[60:66].strip())
                             for line in self.heavy_atom]
            if ligand:
                bfactors += [float(line[60:66].strip())
                             for line in self.heavy_hetatm]
        else:
            if protein:
                bfactors += [float(line[60:66].strip())
                             for line in self.atom]
            if ligand:
                bfactors += [float(line[60:66].strip())
                             for line in self.hetatm]
        return bfactors

    def grab_radius(self, radius, coordinates, include_h=False,
                    protein=True, ligand=False):
        """
        Grabs those atoms that are within a specified
        radius given a 3D-coordinate.

        Parameters
        ----------

        radius : `int` or `float`.
          Radius in Angstroms.

        Coordinates : `list`
          A list of x, y, z coordinates , e.g., `[1.0, 2.4, 4.0]`

        Returns
        ----------

        atom_cont : `list`.
          List of PDB file contents that are within the specified radius.

        """
        in_radius = []
        target_atoms = []

        if include_h:
            if protein:
                target_atoms += self.atom
            if ligand:
                target_atoms += self.hetatm
        else:
            if protein:
                target_atoms = self.atom_no_h
            if ligand:
                target_atoms = self.heavy_hetatm

        for line in target_atoms:
            xyz_coords = self._get_xyz_coords(line)
            distance = (sum([(coordinates[i] - xyz_coords[i])**2
                             for i in range(3)]))**0.5
            if distance <= radius:
                in_radius.append(line)
        return in_radius

    def _get_xyz_coords(self, pdb_line):
        return (float(pdb_line[30:38]),
                float(pdb_line[38:46]),
                float(pdb_line[46:54]))

    def _map_residues(self):
        residue_map = dict()

        target_atoms = self.atom + self.hetatm

        for l in target_atoms:
            if not l[17:26] in residue_map:
                residue_map[l[17:26]] = [l]
            else:
                residue_map[l[17:26]].append(l)
        return residue_map
