# Sebastian Raschka 2016
# Copyright (C) 2016 Michigan State University
#
# siteinterlock, a novel algorithm for protein-ligand
# docking based on graph theory.
#
# Author: Sebastian Raschka <sebastianraschka.com>
# Author email: raschkas@msu.edu
#
# License: GPL v3

from setuptools import setup, find_packages
import siteinterlock

VERSION = siteinterlock.__version__

setup(name='siteinterlock',
      version=VERSION,
      description=('A novel approach to pose selection in'
                   'protein-ligand docking based on graph theory.'),
      author='Sebastian Raschka',
      author_email='raschkas@msu.edu',
      url='https://github.com/psa-lab/siteinterlock',
      packages=find_packages(),
      package_data={'': ['LICENSE', 'README.md', 'requirements.txt']},
      include_package_data=True,
      license='{placeholder}',
      platforms='any',
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Operating System :: MacOS',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Scientific/Engineering',
      ],
      long_description="""

A novel approach to pose selection in protein-ligand
docking based on graph theory.

Contact
=============

SiteInterlock is a Python package for selecting near-native protein-ligand
docking poses based on the hypothesis that interfacial rigidification of
both the protein and ligand prove to be important characteristics of the
native binding mode and are sensitive to the spatial coupling of
interactions and bond-rotational degrees of freedom in the interface.

The `siteinterlock` package is being developed in the
Protein Structure Analysis & Design Laboratory (http://www.kuhnlab.bmb.msu.edu)
at Michigan State University.

The source code is hosted at https://github.com/psa-lab/siteinterlock and
you can contact the original author of this
software package at raschkas@msu.edu. The email address for general questions
about the siteinterlock package, please use the following address:
kuhnlab@msu.edu

""")
