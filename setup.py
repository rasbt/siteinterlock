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
      package_data={'': ['LICENSE', 'README.md'],
                    'scripts': ['get-substructures.py',
                                'proflex_bondviz.py',
                                'proflex_hether.py',
                                'pymol_proflex-color.pml',
                                'pymol_bondvis-plugin.py',
                                'siteinterlock-score.py',
                                'slide_propmap.py']},
      include_package_data=True,
      license='GPLv3',
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
