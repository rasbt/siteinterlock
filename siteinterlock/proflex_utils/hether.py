# Sebastian Raschka 2016
# Copyright (C) 2016 Michigan State University
#
# siteinterlock, a novel algorithm for protein-ligand
# docking based on graph theory.
#
# Author: Sebastian Raschka <http://sebastianraschka.com>
# Author email: mail@sebastianraschka.com
#
# License: GPLv3
import math


def _read_pflexdataset(pflexdataset_file):
    """
    Note: Number of atoms differs from number of atoms in the
    decomp_lst file, since the latter also counts Hetatoms.
    However, this is not an issue in practice since
    Hether is used via SiteInterlock on ligand-free protein
    structures.

    Note: Atom count DOES NOT include hydrophobic tethers.

    """
    saw_hetatm = False
    atom_cnt = 0
    tether_cnt = 0
    calphas = []
    with open(pflexdataset_file, 'r') as in_file:
        for line in in_file:
            line_len = len(line)
            if line and line_len > 15 and line.startswith('ATOM'):
                atom_cnt += 1

                if line[13:15] == "CA":
                    calphas.append(atom_cnt)
            elif line_len >= 6 and line.startswith('HETATM'):
                saw_hetatm = True
                if line_len >= 20 and line[13] == 'X' and line[17:20]:
                    tether_cnt += 1
    return atom_cnt, calphas, tether_cnt


def _read_decomp(decomp_list_file):
    """
    Note: Atom count DOES include hydrophobic tethers.

    # consistency with proflexdataset
    assert(n_atoms - tether_cnt == atom_cnt),
    where atom_cnt comes from pflexdataset
    """

    decomp_dict = {}
    with open(decomp_list_file, 'r') as in_file:
        header_line = next(in_file)
        if not header_line.startswith('HEADER'):
            raise AttributeError('Decomp list file seems to'
                                 ' have an incorrect HEADER')
        header_line = header_line.split()
        n_residues = int(header_line[1])
        n_atoms = int(header_line[2])
        for line in in_file:
            if line.startswith('A: '):
                line = line.split()
                step = int(line[1])
                energy = float(line[2])
                decomp_dict[step] = {'energy': energy, 'clusters': []}
            elif line and not line.startswith(('END', 'B: ')):
                line = [int(s.strip()) for s in line.split(':')]
                decomp_dict[step]['clusters'] += line
    return decomp_dict, n_residues, n_atoms


def _cluster_mapping(calpha_idx, cluster_idx):
    """
    Parameters
    ------------
    calpha_idx : list
       List of integers containing the index positions
       of C-alpha atoms as returned from
       `read_pflexdataset(...)`.
       len(calpha_idx) < len(cluster_idx)
    cluster_idx : list
       List of cluster indeces (integers) as given for
       each decomposition in Proflex's decomp_list file.

    Returns
    ------------
    clusters_count : dict
       A dictionary counting the number of
       C-alpha atoms per cluster index.

    """
    assert(len(calpha_idx) <= len(cluster_idx))

    calpha_clusters = [cluster_idx[idx] for idx in calpha_idx]
    clusters_count = {}
    for idx in calpha_clusters:
        if idx not in clusters_count:
            clusters_count[idx] = 1
        else:
            clusters_count[idx] += 1

    return clusters_count


def _cluster_rigidity(cluster_dict, cluster_threshold=3, how='proportion'):
    """
    Returns proportion of residues in rigid clusters
    """
    how_allowed = set(['proportion', 'count'])
    if how not in how_allowed:
        ValueError('`how must be in %s`' % how_allowed)
    if how == 'count':
        raise NotImplementedError('how="count" not implemented, yet.')

    total_residues = sum([i for i in cluster_dict.values()])
    rigid_residues = sum([i for i in cluster_dict.values()
                          if i >= cluster_threshold])
    rigid_clusters = sum([1 for i in cluster_dict.values()
                          if i >= cluster_threshold])
    return rigid_residues / float(total_residues), rigid_clusters


def _rigidity_diff(thresholds_dict):

    # sort by descending energy thresholds
    pairs = sorted([(j, i) for i, j in thresholds_dict.items()], reverse=True)

    max_diff = -9999
    optim = pairs[0]

    for idx, tup in enumerate(pairs[:-1]):

        # iterates from largest to smallest rigidity

        # pairs[idx][1][0] is rigid_residues / float(total_residues)
        # pairs[idx][1][1] is n_rigid_clusters

        if pairs[idx][1][0] >= 0.9:
            continue

        if pairs[idx][1][0] <= 0.25:
            break

        diff = pairs[idx + 1][1][1] - pairs[idx][1][1]

        if diff > max_diff:
            max_diff = diff
            optim = pairs[idx]

    return optim


def hether(pflexdataset_file, decomp_file, verbose=0):
    pflexd_atom_cnt, pflexd_calphas, pflexd_tether_cnt = \
        _read_pflexdataset(pflexdataset_file)
    dd, n_residues, n_atoms = _read_decomp(decomp_file)

    thresholds_dict = {}
    for i in dd.keys():

        cluster_dict = _cluster_mapping(calpha_idx=pflexd_calphas,
                                        cluster_idx=dd[i]['clusters'])

        rigidity, n_rigid_clusters = _cluster_rigidity(cluster_dict)
        thresholds_dict[(rigidity, n_rigid_clusters)] = dd[i]['energy']

    if verbose:
        for v, k in sorted(thresholds_dict.items(), reverse=True):
            print('Rigidity: %.2f Clusters: %d H-bond Thres.: %.5f'
                  % (v[0], v[1], k))

    opt = _rigidity_diff(thresholds_dict)
    energy, rigidity, n_cluster = opt[0], opt[1][0], opt[1][1]
    return math.ceil(1000.0 * energy) / 1000.0, rigidity, n_cluster
