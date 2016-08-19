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
