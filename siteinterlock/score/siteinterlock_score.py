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

from siteinterlock.pdb import Pdb
from siteinterlock.utils.stats import mean, standardize


def siteinterlock_score(paths):
    p_means, l_means = [], []

    for f in paths:
        pdb = Pdb()
        pdb.read_pdbfile(file_path=f)
        b_prot = pdb.get_bfactors(protein=True, ligand=False, atoms='all')
        b_lig = pdb.get_bfactors(protein=False, ligand=True, atoms='all')
        p_mean, l_mean = mean(b_prot), mean(b_lig)
        p_means.append(p_mean)
        l_means.append(l_mean)

    p_z = standardize(p_means)
    l_z = standardize(l_means)
    s_scores = [(i + j) / 2.0 for i, j in zip(p_z, l_z)]

    return s_scores
