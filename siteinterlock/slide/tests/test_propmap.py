import os
from siteinterlock.slide.propmap import _in_range
from siteinterlock.slide.propmap import _get_mol2_coords
from siteinterlock.slide import propmap


absdir = os.path.dirname(os.path.abspath(__file__))


def test_in_range_1():
    r = _in_range(float1=1.123, float2=1.123, floatmin=0.0, floatmax=0.0)
    assert r is True


def test_in_range_2():
    r = _in_range(float1=1.123, float2=1.124, floatmin=0.0, floatmax=0.0)
    assert r is False


def test_in_range_3():
    r = _in_range(float1=1.123, float2=1.124, floatmin=0.1, floatmax=0.0)
    assert r is True


def test_in_range_4():
    r = _in_range(float1=1.123, float2=1.023, floatmin=0.0, floatmax=0.1)
    assert r is True


def test_get_mol2_coords_1():
    rel_test_data = 'propmap_test_data/1com_crystal.mol2'
    abs_test_data = os.path.join(absdir, rel_test_data)
    expect = [['C1', 52.96, 24.103, 44.966],
              ['C2', 52.329, 22.721, 45.019],
              ['C3', 50.998, 22.565, 45.196],
              ['C4', 50.073, 23.752, 45.247],
              ['C5', 50.669, 24.979, 44.606],
              ['C6', 51.987, 25.098, 44.369],
              ['C7', 54.288, 24.137, 44.192],
              ['C8', 53.532, 24.496, 46.341],
              ['C9', 52.573, 24.963, 47.432],
              ['C10', 52.116, 26.407, 47.329],
              ['O1', 48.879, 23.487, 44.572],
              ['O2', 54.572, 25.142, 43.518],
              ['O3', 55.036, 23.15, 44.272],
              ['O4', 52.072, 24.168, 48.176],
              ['O5', 50.925, 26.67, 47.451],
              ['O6', 52.959, 27.275, 47.125],
              ['H1', 48.331, 24.251, 44.744],
              ['H2', 52.9556, 21.8478, 44.9133],
              ['H3', 50.5905, 21.5705, 45.3028],
              ['H4', 49.897, 23.9381, 46.3168],
              ['H5', 50.0142, 25.7913, 44.3272],
              ['H6', 52.3527, 25.905, 43.7514],
              ['H7', 54.0396, 23.6028, 46.734],
              ['H8', 54.1558, 25.3778, 46.133]]
    r = _get_mol2_coords(abs_test_data)
    assert r == expect


def test_propmap_1():
    rel_test_data1 = 'propmap_test_data/1com_crystal.mol2'
    abs_test_data1 = os.path.join(absdir, rel_test_data1)

    rel_test_data2 = 'propmap_test_data/1com_0.pts'
    abs_test_data2 = os.path.join(absdir, rel_test_data2)
    expect = [('C1', 'hydrophobic contact'),
              ('C3', 'hydrophobic contact'),
              ('C5', 'hydrophobic contact'),
              ('C8', 'hydrophobic contact'),
              ('O1', 'b [H-bond Donor and/or Acceptor]'),
              ('O2', 'a [H-bond Acceptor]'),
              ('O3', 'a [H-bond Acceptor]'),
              ('O4', 'a [H-bond Acceptor]'),
              ('O5', 'a [H-bond Acceptor]'),
              ('O6', 'a [H-bond Acceptor]')]
    r = sorted(propmap(mol2_path=abs_test_data1,
                       pts_path=abs_test_data2).items())
    assert expect == r
