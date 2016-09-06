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
