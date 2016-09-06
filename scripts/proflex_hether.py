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
#
# Author: Sebastian Raschka <http://sebastianraschka.com>
# Author email: mail@sebastianraschka.com
#

from siteinterlock.proflex_utils import hether
from siteinterlock import __version__
import argparse
from time import strftime


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=('HETHER command line interface to determine '
                     '\noptimal hydrogen-bond energy thresholds '
                     '\nfor Proflex analyses.'),
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=('Example:\n'
                'proflex_hether.py'
                ' -i1 1com_proflexdataset'
                ' -i2 decomp_list'))

    parser.add_argument('-i1', '--input1',
                        required=True, help='Proflex Dataset File')
    parser.add_argument('-i2', '--input2',
                        required=True, help='Proflex Decomp List File')

    args = parser.parse_args()

    energy, rigidity, n_cluster = hether(pflexdataset_file=args.input1,
                                         decomp_file=args.input2)

    print('#')
    print('# SiteInterlock version %s' % (__version__))
    print('# Timestamp: %s' % strftime('%Y-%m-%dT%H:%M:%S'))
    print('#')
    print('==============')
    print('HETHER results')
    print('==============')
    print('Suggested energy threshold: %s kcal/mol' % energy)
    print('Number of rigid clusters: %s' % n_cluster)
    print('Relative rigidity [0, 1]: %s\n' % round(rigidity, 2))
