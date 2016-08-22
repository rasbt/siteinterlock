# SiteInterlock

A novel approach to pose selection in protein-ligand docking based on graph theory.

`siteinterlock` is a Python package for selecting near-native protein-ligand
docking poses based upon the hypothesis that interfacial rigidification
of both the protein and ligand prove to be important characteristics of
the native binding mode and are sensitive to the spatial coupling of
interactions and bond-rotational degrees of freedom in the interface.

The `siteinterlock` package was developed in the
Protein Structure Analysis & Design Laboratory (http://www.kuhnlab.bmb.msu.edu)
at Michigan State University. For additional information on the theory
behind the SiteInterlock project, please refer to the accompanying research publication:

- Raschka, Sebastian, Joseph Bemister-Buffington, and Leslie A. Kuhn 2016.
"Detecting the Native Ligand Orientation by Interfacial Rigidity: SiteInterlock."
*Proteins: Structure, Function, and Bioinformatics*
XX (X). John Wiley & Sons : XXX-XX. doi:xx.xxxx/xxxxxxxx.
 {insert link to publisher website}

# Installation

The `siteinterlock` package is compatible with current versions of Python
such as Python 3.2 or newer, and the package itself does not require external
dependencies or libraries. You can find more information on how to obtain
and install Python at https://www.python.org/downloads/.

To produce the input files that are required for the SiteInterlock analysis,
you will need to have MSU ProFlex installed (http://kuhnlab.bmb.msu.edu/software/index.html).
MSU ProFlex (formerly called FIRST) predicts the rigid and flexible regions in a protein structure,
given a Protein Data Bank (PDB) file, including polar hydrogen atoms. You can find more information
about obtaining and installing ProFlex at http://kuhnlab.bmb.msu.edu/software/proflex/index.html.


## Installing siteinterlock from source

You can obtain the latest, stable release of `siteinterlock` from GitHub at https://github.com/psa-lab/siteinterlock/releases.

1. After clicking on the `Source code (zip)` or `Source code (tar.gz)` download links,
please navigate to your download folder and unpack the source code archive using your preferred archive-tool.
2. Next, go into the unzipped `siteinterlock-master` directory,
and install the `siteinterlock`
package by executing `python setup.py install` (inside `siteinterlock-master`).
3. You may verify your installation by opening a new
terminal and executing the following command:
`python -c 'import siteinterlock; print(siteinterlock.__version__)'`, which should print `1.0.0`.
4. Now, you will be able to use the SiteInterlock scripts provided
in the `scripts/` subdirectory from any location on your local drive.


# Documentation

You can find a detailed user guide in the package documentation that
is hosted at http://psa-lab.github.io/siteinterlock/index.html

Alternatively, you can view the documentation offline after
downloading `siteinterlock` and opening the index.html file that is
located in the `docs/html/` subdirectory by opening it in your preferred web browser.
