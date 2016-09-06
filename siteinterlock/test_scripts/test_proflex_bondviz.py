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


def test_bondviz():

    s_path = os.path.join('..', '..',
                          'scripts', 'proflex_bondviz.py')
    e1_path = os.path.join('..', '..',
                           'examples', 'proflex_output',
                           '1com_0057', '1com_0057_pflex_in_proflexdataset')

    abs_script = os.path.join(absdir, s_path)
    abs1_examples = os.path.join(absdir, e1_path)

    r = subprocess.Popen(['python', abs_script,
                          '--input', abs1_examples,
                          '--bonds', 'hbonds'],
                         stdout=subprocess.PIPE).communicate()[0]

    r = [i for i in r.decode("utf-8").split('\n')]
    r = [i for i in r if i and not i.startswith('#')]
    expect = ['Atom#1 Atom#2', '1951 3761', '1949 3755',
              '3269 3759', '3566 3755', '3266 3761', '1185 3765']

    assert r == expect, r
