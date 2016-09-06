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
import shutil


absdir = os.path.dirname(os.path.abspath(__file__))


def test_hether():

    s_path = os.path.join('..', '..',
                          'scripts', 'proflex_hether.py')
    e1_path = os.path.join('..', '..',
                           'examples', 'proflex_output',
                           '1com_nolig', '1com_nolig_proflexdataset')
    e2_path = os.path.join('..', '..',
                           'examples', 'proflex_output',
                           '1com_nolig', 'decomp_list')

    abs_script = os.path.join(absdir, s_path)
    abs1_examples = os.path.join(absdir, e1_path)
    abs2_examples = os.path.join(absdir, e2_path)

    r = subprocess.Popen(['python', abs_script,
                          '--input1', abs1_examples,
                          '--input2', abs2_examples],
                         stdout=subprocess.PIPE).communicate()[0]

    r = [i for i in r.decode("utf-8").split('\n')]
    r = [i for i in r if i and not i.startswith('#')]
    expect = ['==============', 'HETHER results', '==============',
              'Suggested energy threshold: -0.806 kcal/mol',
              'Number of rigid clusters: 4',
              'Relative rigidity [0, 1]: 0.83']

    assert r == expect
