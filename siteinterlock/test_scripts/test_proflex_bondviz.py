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
