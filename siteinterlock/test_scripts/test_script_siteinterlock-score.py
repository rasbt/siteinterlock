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
import subprocess


absdir = os.path.dirname(os.path.abspath(__file__))


def test_scoring():

    s_path = os.path.join('..', '..',
                          'scripts', 'siteinterlock-score.py')
    e_path = os.path.join('..', '..',
                          'examples', 'proflex_output',
                          'all-docking-poses-pdbs-9A')

    abs_script = os.path.join(absdir, s_path)
    abs_examples = os.path.join(absdir, e_path)

    r = subprocess.Popen(['python', abs_script,
                          '-i', abs_examples],
                         stdout=subprocess.PIPE).communicate()[0]
    r = [i for i in r.decode("utf-8").split('\n')]
    r = [i for i in r if i and not i.startswith('#')]

    expect = ['Filename,SiteInterlock_Score',
              '1com_0057_pflex_in_flex_0001.pdb,-1.094',
              '1com_crystal_pflex_in_flex_0001.pdb,-1.053',
              '1com_0140_pflex_in_flex_0001.pdb,-0.357',
              '1com_0058_pflex_in_flex_0001.pdb,-0.087',
              '1com_0119_pflex_in_flex_0001.pdb,-0.070',
              '1com_1_0066_pflex_in_flex_0001.pdb,0.776',
              '1com_0130_pflex_in_flex_0001.pdb,1.885']

    assert r == expect
