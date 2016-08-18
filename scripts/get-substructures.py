from siteinterlock.pdb import Pdb
import argparse
import os


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Extracts a protein substructure based '
                    'on atoms surrounding a ligand\'s heavy atoms.',
        epilog='Example:\n'
               'python get-substructures.py -i ./test_input_files/pdb_1.pdb '
               '-o ~/Desktop/substructure_1.pdb -l PRE\n',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--input', type=str, metavar='PDB',
                        help='Target PDB structure'
                        'containing .pdb files.', required=True)
    parser.add_argument('-o', '--output', type=str, metavar='PDB',
                        help="Path to the output PDB file",
                        required=True)
    parser.add_argument('-l', '--ligand_name', type=str, metavar='RES',
                        help="Residue name of the binding site ligand",
                        required=True)

    parser.add_argument('-a', '--apply_to_dir', action='store_true',
                        default=False, help="Treats --output and "
                        "--input as directories (default: False)")
    parser.add_argument('-r', '--radius', type=float, default=9.0,
                        help="Radius around ligand's "
                             "heavy atoms (default: 9.0)")

    args = parser.parse_args()

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
                   a[17:20] == args.ligand_name]
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
