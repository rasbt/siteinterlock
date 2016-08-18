# Sebastian Raschka 2016
# Copyright (C) 2016 Michigan State University
#
# siteinterlock, a novel algorithm for protein-ligand
# docking based on graph theory.
#
# Author: Sebastian Raschka <sebastianraschka.com>
# Author email: raschkas@msu.edu
#
# License: GPLv3

import os


class Mol2():
    """ Object that allows operations with protein files in PDB format. """
    def __init__(self, file_cont):
        self.cont = []
        self.atom = []
        self.bond = []

        if not file_cont:
            return None
        if isinstance(file_cont, list):
            self.cont = file_cont[:]
        elif os.path.isfile(file_cont):
            self.cont = self.read_mol2(file_cont)

        if self.cont:
            self.atom = self.get_atomsection()
            self.bond = self.get_bondsection()

        return None

    def read_mol2(self, file_path):
        """ Reads mol2 file contents to a list. """
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

    def get_atomsection(self, mol2_list=None):
        """ Reads atom section from a mol2 file content list."""
        return self._get_section(section='ATOM', mol2_list=None)

    def get_bondsection(self, mol2_list=None):
        """ Reads bond section from a mol2 file content list."""
        return self._get_section(section='BOND', mol2_list=None)

    def get_coords(self, mol2_list=None, heavy=False):
        """ Returns 3D coordinates as list of floats. """
        if not mol2_list:
            mol2_list = self.atom

        coords = []
        for line in mol2_list:
            x, y, z, atm = line.split()[2:6]
            if heavy and atm == 'H':
                continue
            coords.append((float(x), float(y), float(z)))
        return coords
