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

from siteinterlock.slide_utils import propmap
from siteinterlock import __version__
import argparse
from time import strftime


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=('SLIDE-propmap command line interface to extract '
                     '\nhydrogen-bond acceptor and donor information '
                     '\nfor Proflex analyses.'),
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=('Example:\n'
                'slide-propmap.py'
                ' -i1 ligand.mol2'
                ' -i2 ligand.pts'))

    parser.add_argument('-i1', '--input1',
                        required=True, help='Ligand MOL2 file')
    parser.add_argument('-i2', '--input2',
                        required=True, help='Ligand PTS file from SLIDE')

    args = parser.parse_args()

    mapping = sorted(propmap(mol2_path=args.input1,
                             pts_path=args.input2).items())

    print('#')
    print('# SiteInterlock version %s' % (__version__))
    print('# Timestamp: %s' % strftime('%Y-%m-%dT%H:%M:%S'))
    print('#')
    print('================')
    print('PROPMAP results')
    print('================')
    for atom in mapping:
        print('%s --> %s' % (atom[0], atom[1]))
    print('\n')
