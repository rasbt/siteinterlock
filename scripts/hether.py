# Sebastian Raschka 2016
# Copyright (C) 2016 Michigan State University
#
# siteinterlock, a novel algorithm for protein-ligand
# docking based on graph theory.
#
# Author: Sebastian Raschka <sebastianraschka.com>
# Author email: raschkas@msu.edu
#
# License: GPLv3

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
                'hether.py'
                ' -i1 1hwr_proflexdataset'
                ' -i2 decomp_list'))

    parser.add_argument('-i1', '--input1',
                        required=True, help='Proflex Dataset File')
    parser.add_argument('-i2', '--input2',
                        required=True, help='Proflex Decomp List File')

    args = parser.parse_args()

    energy, rigidity, n_cluster = hether(pflexdataset_file=args.input1,
                                         decomp_file=args.input2)

    print('\nSiteInterlock version %s' % (__version__))
    print('Author: Sebastian Raschka')
    print('Timestamp: %s' % strftime('%Y-%m-%dT%H:%M:%S'))
    print('\n==============')
    print('HETHER results')
    print('==============')
    print('Suggested energy threshold: %s kcal/mol' % energy)
    print('Number of rigid clusters: %s' % n_cluster)
    print('Relative rigidity [0, 1]: %s\n'
           % round(rigidity, 2))
