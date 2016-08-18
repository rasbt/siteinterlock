# SLIDE-propmap command line interface
# Sebastian Raschka, 2016

import argparse
import os
from siteinterlock.pflex.bondviz import get_ligand_atoms
from siteinterlock.pflex.bondviz import get_bonded_atoms
from siteinterlock.pflex.bondviz import write_bonded_list
from siteinterlock.pflex.bondviz import print_bonded_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=('Returns the atom numbers of hydrogen-bonded'
                     'ligand-protein pairs from a ProFlex dataset file.'),
        epilog=('Example:\n'
                'grab_bonds_proflexdataset.py ~/Desktop/x_proflexdataset\n'),
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--input', help='Input proflex dataset file')
    parser.add_argument('-o', '--output', help='Output file (optional)')
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

    if args.output:
        with open(args.output, 'w') as outf:
            write_bonded_list(bonded_atoms, outf)
    else:
        print_bonded_list(bonded_atoms)
