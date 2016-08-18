# SLIDE-propmap command line interface
# Sebastian Raschka, 2016

from siteinterlock.slide import propmap
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

    print('\nSiteInterlock version %s' % (__version__))
    print('Author: Sebastian Raschka')
    print('Timestamp: %s' % strftime('%Y-%m-%dT%H:%M:%S'))
    print('\n================')
    print('PROPMAP results')
    print('================')
    for atom in mapping:
        print('%s --> %s' % (atom[0], atom[1]))
    print()
