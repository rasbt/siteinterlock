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
import json

from siteinterlock.mol2 import Mol2


absdir = os.path.dirname(os.path.abspath(__file__))

mol1_cont = ['@<TRIPOS>MOLECULE\n',
             'mol2_file1\n',
             '   9    9     0     0     0\n',
             'SMALL\n',
             'USER_CHARGES\n',
             '\n',
             'mmff94s_NoEstat = 44.88\n',
             '@<TRIPOS>ATOM\n', '      1 C1         -5.0187   -7.8208'
             '   -3.4745 C.ar      1 <0>        -0.0736\n',
             '      2 C2         -7.1625   -6.7138   -3.3495 C.ar'
             '      1 <0>        -0.0770\n', '      3 C3         -5.5821'
             '   -8.8226   -4.2649 C.ar      1 <0>        -0.1229\n',
             '      4 C4         -7.7259   -7.7155   -4.1400 C.ar'
             '      1 <0>        -0.1228\n', '      5 C5         -4.1476'
             '   -5.8652   -1.3128 C.2       1 <0>        -0.1743\n',
             '      6 C6         -5.8090   -6.7664   -3.0167 C.ar'
             '      1 <0>        -0.0550\n', '      7 C7         -6.9356'
             '   -8.7699   -4.5977 C.ar      1 <0>        -0.0597\n',
             '      8 C8         -5.2277   -5.7330   -2.2025 C.2       1 <0>'
             '         0.1456\n', '      9 C9         -3.9942   -4.6054'
             '   -0.7974 C.2       1 <0>         0.0377\n', '@<TRIPOS>BOND\n',
             '     1    1    3 ar\n', '     2    1    6 ar\n', '     3    2 '
             '   4 ar\n', '     4    2    6 ar\n', '     5    3    7 ar\n',
             '     6    4    7 ar\n', '     7    5    8 1\n',
             '     8    5    9 2\n', '     9    6    8 1\n']

mol1_atom = ['      1 C1         -5.0187   -7.8208   -3.4745 C.ar'
             '      1 <0>        -0.0736\n', '      2 C2         -7.1625'
             '   -6.7138   -3.3495 C.ar      1 <0>        -0.0770\n',
             '      3 C3         -5.5821   -8.8226   -4.2649 C.ar'
             '      1 <0>        -0.1229\n', '      4 C4         -7.7259'
             '   -7.7155   -4.1400 C.ar      1 <0>        -0.1228\n',
             '      5 C5         -4.1476   -5.8652   -1.3128 C.2       1 <0>'
             '        -0.1743\n', '      6 C6         -5.8090   -6.7664'
             '   -3.0167 C.ar      1 <0>        -0.0550\n', '      7 C7'
             '         -6.9356   -8.7699   -4.5977 C.ar      1 <0>'
             '        -0.0597\n', '      8 C8         -5.2277   -5.7330'
             '   -2.2025 C.2       1 <0>         0.1456\n', '      9 C9'
             '         -3.9942   -4.6054   -0.7974 C.2       1 <0>'
             '         0.0377\n']

mol1_bond = ['     1    1    3 ar\n', '     2    1    6 ar\n',
             '     3    2    4 ar\n', '     4    2    6 ar\n',
             '     5    3    7 ar\n', '     6    4    7 ar\n',
             '     7    5    8 1\n', '     8    5    9 2\n',
             '     9    6    8 1\n']


def test_init_none():
    mol2 = Mol2()
    assert mol2.cont == []
    assert mol2.atom == []
    assert mol2.bond == []


def test_init_path():
    rel_test_data = 'mol2_test_data/mol1.mol2'
    abs_test_data = os.path.join(absdir, rel_test_data)
    mol2 = Mol2(abs_test_data)
    assert mol2.cont == mol1_cont
    assert mol2.atom == mol1_atom
    assert mol2.bond == mol2.bond
