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

import os
import argparse
from time import strftime
from siteinterlock.score import siteinterlock_score
from siteinterlock import __version__

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=('SiteInterlock Scoring'),
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=('Example:\n'
                'siteinterlock_score.py'
                ' -i all-docking-poses-pdbs-9A'))

    parser.add_argument('-i', '--input_dir',
                        required=True, help='Input directory containing'
                                            ' ProFlex output PDB files.')

    args = parser.parse_args()

    paths = [os.path.join(args.input_dir, i)
             for i in os.listdir(args.input_dir) if i.endswith('.pdb')]
    scores = siteinterlock_score(paths=paths)

    print('#')
    print('# SiteInterlock version %s' % (__version__))
    print('# Timestamp: %s' % strftime('%Y-%m-%dT%H:%M:%S'))
    print('#')
    print('# ==============================')
    print('# SiteInterlock Scoring Results')
    print('# ==============================')
    print('Filename,SiteInterlock_Score')
    tup = sorted([(j, i) for i, j in zip(paths, scores)])
    for j, i in tup:
        print('%s,%.3f' % (os.path.basename(i), j))
