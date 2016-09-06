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
#
# Author: Sebastian Raschka <http://sebastianraschka.com>
# Author email: mail@sebastianraschka.com
#

import argparse
import os
from siteinterlock.proflex_utils.bondviz import get_ligand_atoms
from siteinterlock.proflex_utils.bondviz import get_bonded_atoms
from siteinterlock.proflex_utils.bondviz import write_bonded_list
from siteinterlock.proflex_utils.bondviz import print_bonded_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=('Returns the atom numbers of hydrogen-bonded'
                     'ligand-protein pairs from a ProFlex dataset file.'),
        epilog=('Example:\n'
                'grab_bonds_proflexdataset.py ~/Desktop/x_proflexdataset\n'),
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--input', help='Input proflex dataset file')
    parser.add_argument('-b', '--bonds', help='Which bonds to '
                        'write {hbonds, saltbridges, hydrophic, all} '
                        '(the default is "hbonds")',
                        default='hbonds')

    args = parser.parse_args()

    if not args.input:
        parser.print_help()
        print('\n\nPlease provide an input file.\n\n')
        quit()

    if not os.path.isfile(args.input):
        parser.print_help()
        print('\n\nFile does not exist.\n\n')
        quit()

    if args.bonds not in ('hbonds', 'saltbridges', 'hydrophobic', 'all'):
        parser.print_help()
        print('\n\nInvalid argument for --bonds\n\n')
        quit()

    lig_atoms = get_ligand_atoms(args.input)
    bonded_atoms = get_bonded_atoms(args.input, lig_atoms, args.bonds)

    print_bonded_list(bonded_atoms)
