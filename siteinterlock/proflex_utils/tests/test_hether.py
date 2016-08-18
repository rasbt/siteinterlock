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
import json

from siteinterlock.proflex_utils import hether
from siteinterlock.proflex_utils.hether import _read_pflexdataset
from siteinterlock.proflex_utils.hether import _read_decomp
from siteinterlock.proflex_utils.hether import _cluster_mapping
from siteinterlock.proflex_utils.hether import _cluster_rigidity
from siteinterlock.proflex_utils.hether import _rigidity_diff

absdir = os.path.dirname(os.path.abspath(__file__))

N_ATOMS = None
TETHER_CNT = None


def test_read_pflexdataset():
    rel_test_data = 'hether_test_data/hether_testcase_0/1RA1_H_proflexdataset'
    abs_test_data = os.path.join(absdir, rel_test_data)
    pflexd_atom_cnt, pflexd_calphas, pflexd_tether_cnt = \
        _read_pflexdataset(abs_test_data)

    assert(pflexd_atom_cnt == 2489)
    assert(pflexd_tether_cnt == 291)
    assert(len(pflexd_calphas) == 159)
    assert(pflexd_calphas[:3] == [2, 21, 40])


def test_read_decomp():
    rel_test_data = 'hether_test_data/hether_testcase_0/decomp_list'
    abs_test_data = os.path.join(absdir, rel_test_data)
    dd, n_residues, n_atoms = _read_decomp(abs_test_data)

    assert(len(dd) == 131)
    assert(len(dd[0]['clusters']) == 2780)
    assert(dd[0]['energy'] == -9.80474), dd[0]['energy']
    assert(dd[0]['clusters'][:3] == [636, 635, 266])
    assert(n_residues == 159)
    assert(n_atoms == 2780)


def test_cluster_mapping():
    rel_test_data = 'hether_test_data/hether_testcase_0/decomp_dict.json'
    abs_test_data = os.path.join(absdir, rel_test_data)
    with open(abs_test_data, 'r') as t:
        s = t.read()
        dd = json.loads(s)
        dd = {int(k): v for k, v in dd.items()}

    rel_test_data = 'hether_test_data/hether_testcase_0/calphas.json'
    abs_test_data = os.path.join(absdir, rel_test_data)
    with open(abs_test_data, 'r') as t:
        s = t.read()
        calphas = json.loads(s)

    for i in dd.keys():
        cluster_dict = _cluster_mapping(calpha_idx=calphas,
                                        cluster_idx=dd[i]['clusters'])
        assert(sum([i for i in cluster_dict.values()]) == 159)


def test_cluster_rigidity():
    rel_test_data = 'hether_test_data/hether_testcase_0/cluster_dict.json'
    abs_test_data = os.path.join(absdir, rel_test_data)
    with open(abs_test_data, 'r') as t:
        s = t.read()
        cluster_dict = json.loads(s)
    rig, n_clust = _cluster_rigidity(cluster_dict=cluster_dict)
    assert(round(rig, 3) == 0.849)
    assert(n_clust == 2)


def test_hether():
    rel_test_data = 'hether_test_data/hether_testcase_0/1RA1_H_proflexdataset'
    pflexdataset = os.path.join(absdir, rel_test_data)
    rel_test_data = 'hether_test_data/hether_testcase_0/decomp_list'
    decomplist = os.path.join(absdir, rel_test_data)

    energy, rigidity, n_cluster = hether(pflexdataset_file=pflexdataset,
                                         decomp_file=decomplist)

    assert(n_cluster == 2)
    assert(round(rigidity, 2) == 0.82)
    assert(energy == -0.711), energy


def test_hether_1ahc():
    rel_test_data = ('hether_test_data/hether_testcase_1ahc/'
                     '1ahc_no_lig_proflexdataset')
    pflexdataset = os.path.join(absdir, rel_test_data)
    rel_test_data = 'hether_test_data/hether_testcase_1ahc/decomp_list'
    decomplist = os.path.join(absdir, rel_test_data)
    energy, rigidity, n_cluster = hether(pflexdataset_file=pflexdataset,
                                         decomp_file=decomplist)

    assert(n_cluster == 3)
    assert(round(rigidity, 2) == 0.76)
    assert(energy == -0.393)


def test_hether_1a9x():
    rel_test_data = ('hether_test_data/hether_testcase_1a9x/'
                     '1A9X_nolig_proflexdataset')
    pflexdataset = os.path.join(absdir, rel_test_data)
    rel_test_data = 'hether_test_data/hether_testcase_1a9x/decomp_list'
    decomplist = os.path.join(absdir, rel_test_data)

    energy, rigidity, n_cluster = hether(pflexdataset_file=pflexdataset,
                                         decomp_file=decomplist)

    assert(n_cluster == 5)
    assert(round(rigidity, 2) == 0.83)
    assert(energy == -0.292)
