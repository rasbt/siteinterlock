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


import os
import sys


def mean(lst):
    n = len(lst)
    if not n:
        return None
    return sum(lst) / float(n)


def variance(lst, mu=None):
    n = len(lst)
    if not n:
        return None
    if mu is None:
        mu = mean(lst)
    dev = sum([((i - mu)**2) for i in lst])
    return dev / float(n)


def std_dev(lst, mu=None):
    return variance(lst, mu=mu)**0.5


def standardize(lst):
    mu = mean(lst)
    sigma = std_dev(lst, mu=mu)
    z = [(i - mu) / sigma for i in lst]
    return z
