# Sebastian Raschka 2016
#
# siteinterlock, a novel algorithm for protein-ligand
# docking based on graph theory.
#
# Author: Sebastian Raschka <sebastianraschka.com>
#
# License: {placeholder}

from setuptools import setup, find_packages
import siteinterlock

VERSION = siteinterlock.__version__

setup(name='siteinterlock',
      version=VERSION,
      description='{placeholder}',
      author='Sebastian Raschka',
      author_email='raschkas@msu.edu',
      url='https://github.com/rasbt/siteinterlock',
      packages=find_packages(),
      package_data={'': ['LICENSE', 'README.md', 'requirements.txt']},
      # package_data={'': ['LICENSE', 'README.md', 'requirements.txt']
      # },
      include_package_data=True,
      license='{placeholder}',
      platforms='any',
      classifiers=[
             # 'License :: OSI Approved :: BSD License',
             'Operating System :: Microsoft :: Windows',
             'Operating System :: POSIX',
             'Operating System :: Unix',
             'Operating System :: MacOS',
             'Programming Language :: Python :: 3',
             'Programming Language :: Python :: 3.3',
             'Programming Language :: Python :: 3.4',
             'Programming Language :: Python :: 3.5',
             'Topic :: Scientific/Engineering',
      ],
      long_description="""

{placeholder}


Contact
=============

If you have any questions or comments about siteinterlock,
please feel free to contact me via
eMail: mail@sebastianraschka.com

This project is hosted at https://github.com/rasbt/siteinterlock

The documentation can be found at {placeholder}

""")
