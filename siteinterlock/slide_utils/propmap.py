# Sebastian Raschka 2016
# Copyright (C) 2016 Michigan State University
#
# siteinterlock, a novel algorithm for protein-ligand
# docking based on graph theory.
#
# Author: Sebastian Raschka <http://sebastianraschka.com>
# Author email: mail@sebastianraschka.com
#
# License: GPLv3


def _in_range(float1, float2, floatmin=0.0, floatmax=0.0):
    """Tests if a float1 is in float2 +/- **"""
    upper = float2 + floatmax
    lower = float2 - floatmin
    return (float1 <= upper and float1 >= lower)


def propmap(mol2_path, pts_path):
    """
    """

    slide_to_pflex = {'H': 'hydrophobic contact',
                      'D': 'd [H-bond Donor]',
                      'A': 'a [H-bond Acceptor]',
                      'N': 'b [H-bond Donor and/or Acceptor]'}

    with open(pts_path, 'r') as f:
        pts_cont = []
        for line in f:
            line = line.strip()
            if line:
                cont = line.split()[1:-1]
                # cont should be sth. like
                # ['D', 28.278, 22.089, 42.163]
                cont[0] = slide_to_pflex[cont[0]]
                cont[1:] = [float(i) for i in cont[1:]]
                pts_cont.append(cont)

    mol2_coords = _get_mol2_coords(mol2_path)

    mapped = dict()
    r = 0.004
    for pts in pts_cont:
        for mol2 in mol2_coords:
            if (_in_range(pts[1], mol2[1], r, r) and
                    _in_range(pts[2], mol2[2], r, r) and
                    _in_range(pts[3], mol2[3], r, r)):
                mapped[mol2[0]] = pts[0]

    return mapped


def _get_mol2_coords(mol2_path):
    """Gets processed lines for propmap() function from .mol2 file."""

    with open(mol2_path, 'r') as f:
        mol2_cont = [line.rstrip("\n") for line in f]

    # get Mol2 atom section, i.e., lines after @<TRIPOS>ATOM
    raw_atoms = []
    i = 0
    for line in mol2_cont:
        if "@<TRIPOS>ATOM" in line:
            i += 1
            break
        i += 1
    raw_atoms = mol2_cont[i:]

    # remove everything after the coordinate section
    i = 0
    for line in raw_atoms:
        if "@" in line:
            break
        i += 1
    raw_atoms = raw_atoms[:i]

    clean_atoms = []
    for line in raw_atoms:
        line = line.split()[1: 5]
        i = 1
        while i < len(line):
            line[i] = float(line[i])
            i += 1
        clean_atoms.append(line)

    return clean_atoms
