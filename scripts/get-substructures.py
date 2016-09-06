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

from siteinterlock.pdb import Pdb
import argparse
import os
import sys


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Extracts a protein substructure based '
                    'on atoms surrounding a ligand\'s heavy atoms.',
        epilog='Example:\n'
               'python get-substructures.py -i ./test_input_files/pdb_1.pdb '
               '-o ~/Desktop/substructure_1.pdb -l "PRE,A,234"\n',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--input', type=str, metavar='PDB',
                        help='Target PDB structure', required=True)
    parser.add_argument('-o', '--output', type=str, metavar='PDB',
                        help="Path to the output PDB file",
                        required=True)
    parser.add_argument('-l', '--ligand_name', type=str,
                        metavar='NAME,CHAIN,NUM',
                        help="Information about the binding site ligand in\n"
                        "the PDB file following the format "
                        "<residue_name,chain_ID,residue_number>.\n"
                        "For example, if PRE is the 3-letter specifier of\n"
                        "a prephenic acid ligand, its chain ID is A, and its\n"
                        "residue number is 234, we would provide the input: "
                        "\"PRE,A,234\"\nIf the ligand does not have a chain ID"
                        "\nassigned to it, you can omit it; for example "
                        "\"PRE,A,234\".\n",
                        required=True)

    parser.add_argument('-a', '--apply_to_dir', action='store_true',
                        default=False, help="Treats --output and "
                        "--input as directories (default: False)")
    parser.add_argument('-r', '--radius', type=float, default=9.0,
                        help="Radius around ligand's "
                             "heavy atoms in Angstroms (default: 9.0)")

    args = parser.parse_args()

    res_info = args.ligand_name.split(',')
    if len(res_info) != 3:
        raise AttributeError('Please make sure that you'
                             ' specified the ligand correctly.')
    resi, chain, num = res_info
    if not chain:
        chain = ' '
    while len(num) < 4:
        num = ' ' + num

    if args.apply_to_dir:
        template_proteins = [os.path.join(args.input, f)
                             for f in os.listdir(args.input)
                             if f.endswith('.pdb')]
        if not os.path.isdir(args.output):
            os.mkdir(args.output)
        output_pdbs = [os.path.join(args.output, f)
                       for f in os.listdir(args.input)
                       if f.endswith('.pdb')]

    else:
        template_proteins = [args.input]
        output_pdbs = [args.output]

    for ts, output in zip(template_proteins, output_pdbs):

        tar_prot = Pdb().read_pdbfile(ts)
        tar_lig = [a for a in tar_prot.heavy_hetatm if
                   a[17:20] == resi and
                   a[21:22] == chain and
                   a[22:26] == num]

        a = tar_prot.heavy_hetatm[0]
        if not tar_lig:
            raise AttributeError('Could not find ligand in the PDB file')
        lig_coords = [tar_prot._get_xyz_coords(l)
                      for l in tar_lig]

        target_atoms = set()
        for c in lig_coords:
            target_atoms = target_atoms.union({l for l in
                                              tar_prot.grab_radius(
                                                  radius=args.radius,
                                                  coordinates=c,
                                                  include_h=True)})

        target_atoms = target_atoms.union(tar_lig)

        with open(output, 'w') as out_file:
            for line in sorted(target_atoms):
                out_file.write(line + '\n')
