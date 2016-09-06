# Sebastian Raschka 2016
#
# `siteinterlock` is a Python package for selecting near-native protein-ligand
# docking poses based upon the hypothesis that interfacial rigidification
# of both the protein and ligand prove to be important characteristics of
# the native binding mode and are sensitive to the spatial coupling of
# interactions and bond-rotational degrees of freedom in the interface.
#
# Copyright (C) 2016 Michigan State University
# License: GPLv3
#
# SiteInterlock was developed in the
# Protein Structural Analysis & Design Laboratory
# (http://www.kuhnlab.bmb.msu.edu)
# Contact email: kuhnlab@msu.edu
#
# Package author: Sebastian Raschka <http://sebastianraschka.com>
#


import os


class Mol2():
    """ Object that allows operations with protein files in MOL2 format.

    Parameters
    ------------
    file_cont : list or str
      Python list of MOL2 file contents (each string in the list represents one
      line in the MOL2 file.) or path to a valid MOL2 file.

    Attributes
    -----------
    cont : list
      Python list of MOL2 file contents (each string in the list represents one
      line in the MOL2 file.)
    atom : list
      Python list of MOL2 file contents from the ATOM section
    bond : list
      Python list of MOL2 file contents from the BOND section

    """
    def __init__(self, file_cont=None):
        self.cont = []
        self.atom = []
        self.bond = []

        if isinstance(file_cont, list):
            self.cont = file_cont[:]
        elif isinstance(file_cont, str) and os.path.isfile(file_cont):
            self.cont = self.read_mol2(file_cont)

        if self.cont:
            self.atom = self.get_atomsection()
            self.bond = self.get_bondsection()

    def read_mol2(self, file_path):
        """ Reads mol2 file contents to a list.

        Parameters
        ------------
        file_path : str
          Path to a MOL2 file.

        Returns
        ------------
        cont : list
          Python list of MOL2 file contents
          (each string in the list represents one
          line in the MOL2 file.)
        """
        out = []
        with open(file_path, 'r') as mol2_file:
            for line in mol2_file:
                out.append(line)
        return out

    def _get_section(self, section, mol2_list=None):
        """ Reads atom section from a mol2 file content list."""
        if not mol2_list:
            mol2_list = self.cont

        out = []
        start_pos = 0
        for idx, line in enumerate(mol2_list):
            if line.startswith('@<TRIPOS>%s' % (section)):
                start_pos = idx + 1
                break
        for line in mol2_list[start_pos:]:
            if line.startswith('@<TRIPOS>'):
                break
            if line.strip():
                out.append(line)
        return out

    def get_atomsection(self):
        """ Reads ATOM section from the mol2 file content list `Mol2.cont`.

        Returns
        ------------
        atoms : list
          Python list of MOL2 file contents from the ATOM section
          (each string in the list represents one
          line in the MOL2 file.)

        """
        return self._get_section(section='ATOM', mol2_list=None)

    def get_bondsection(self):
        """ Reads BOND section from the mol2 file content list `Mol2.cont`.

        Returns
        ------------
        bonds : list
          Python list of MOL2 file contents from the BOND section
          (each string in the list represents one
          line in the MOL2 file.)

        """
        return self._get_section(section='BOND', mol2_list=None)

    def get_coords(self, mol2_list=None, heavy_only=False):
        """ Returns 3D coordinates as list of floats.

        Attributes
        -----------
        mol2_list : list or None (default: None)
          Optional list of mol2 file contents from the ATOM section.
          If `None`, uses the atom coordinates from Mol2.atom.
        heavy_only : bool (default: False)
          Ignores non-heavy atoms (i.e., hydrogen atoms) if set to True

        Returns
        ------------
        coords : list
          3D coordinates as a list of floats
        """
        if mol2_list is None:
            mol2_list = self.atom

        coords = []
        for line in mol2_list:
            x, y, z, atm = line.split()[2:6]
            if heavy_only and atm == 'H':
                continue
            coords.append((float(x), float(y), float(z)))
        return coords
