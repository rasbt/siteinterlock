import os.path


def get_ligand_atoms(proflex_dataset):
    """
    Collects atom numbers of the ligand(s) from the Proflex dataset
     and returns them as a list of integers

    Parameters
    ----------
    proflex_dataset : str:
        Path to the proflex_dataset file.

    bonds: str {hbonds, saltbridges, hydrophic, all}

    Returns
    ----------
    atom_list: array-like [n_atoms]
        List of atom numbers of the ligand as integers.

    """
    atom_list = list()
    with open(proflex_dataset, "r") as pdbfile:
        for line in pdbfile:
            line = line.strip()
            if line[0:6] == "HETATM" and line[17:20] != "XXX":
                try:
                    atom_num = int(line[6:11])
                    atom_list.append(atom_num)
                except ValueError:
                    continue
    return atom_list

def get_bonded_atoms(proflex_dataset, atom_list, bonds):
    """
    Collects atom numbers of bonded ligand and protein atoms
    from the proflex_dataset output file.

    Parameters
    ----------
    proflex_dataset : str:
        Path to the proflex_dataset file.
    atom_list: array-like [n_atoms]
        List of atom numbers of the ligand as integers.

    Returns
    ----------
    bond pairs: array-like [n_atoms, n_pairs]
        List of sublists of the bonded atoms

    """
    bond_pairs = list()
    with open(proflex_dataset, "r") as pdata:
        for line in pdata:
            line = line.strip()
            if line[0:9] == "REMARK:HB":
                if bonds == 'hbonds' and line[55:57] != 'HB':
                    continue
                if bonds == 'hydrophobic' and line[55:57] != 'PH':
                    continue
                if bonds == 'saltbridges' and line[55:57] != 'SB':
                    continue
                columns = line.split()
                if int(columns[4]) in atom_list or int(columns[5]) in atom_list:
                    bond_pairs.append([int(columns[4]), int(columns[5])])
    return bond_pairs

def print_bonded_list(bond_pairs):
    """ Prints atom numbers of bonded pairs to the screen in 2 columns """
    print("Atom#1 Atom#2")
    for pair in bond_pairs:
        print("{} {}".format(pair[0], pair[1]))

def write_bonded_list(bond_pairs, fileobj):
    """ Prints atom numbers of bonded pairs to the screen in 2 columns """
    if len(bond_pairs) > 0:
        if len(bond_pairs) > 1:
            for pair in bond_pairs[:-1]:
                fileobj.write("{} {}\n".format(pair[0], pair[1]))
        fileobj.write("{} {}".format(bond_pairs[-1][0], bond_pairs[-1][1]))
