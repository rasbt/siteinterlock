siteinterlock version: 1.0.0 
## Pdb

*Pdb()*

Object that allows operations with protein files in PDB format.

### Methods

<hr>

*get_bfactors(protein=True, ligand=False, atoms='all')*

Collects b-factors (temperature factors) from ATOM
    and/or HETATM entries in a list.

**Parameters**

- `protein` : `bool`.

    If `True`, includes ATOM entries in calculation.


- `ligand` : `bool`.

    If `True`, includes HETATM entries in calculation.


- `atoms` : `str` (default: `'all'`)

    A string `'all'`, `'mainchain'`, `'calpha'`
    `"all"`: Includes all atoms in the RMSD calculation.
    `"mainchain"`: Only considers protein mainchain atoms (N, CA, O, C).
    `"calpha"`: Only considers C-alpha protein atoms.
    `"heavy"`: Only considers all atoms but hydrogen.

**Returns**

- `bfactors` : `list`

    B-factors as floats in a list.

<hr>

*grab_radius(radius, coordinates, include_h=False, protein=True, ligand=False)*

Grabs those atoms that are within a specified
    radius given a 3D-coordinate.

**Parameters**


- `radius` : `int` or `float`.

    Radius in Angstroms.


- `Coordinates` : `list`

    A list of x, y, z coordinates , e.g., `[1.0, 2.4, 4.0]`

**Returns**


- `atom_cont` : `list`.

    List of PDB file contents that are within the specified radius.

<hr>

*read_pdbfile(file_path)*

None

