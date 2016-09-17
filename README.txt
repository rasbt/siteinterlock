# SiteInterlock

***A novel approach to pose selection in protein-ligand docking based on graph theory.***

`siteinterlock` is a Python package for selecting near-native protein-ligand
docking poses based upon the hypothesis that interfacial rigidification
of the protein-ligand interface is an important characteristic that can detect
the native ligand binding mode.

The `siteinterlock` package was developed by Sebastian Raschka in the
Protein Structural Analysis & Design Laboratory (http://www.kuhnlab.bmb.msu.edu)
at Michigan State University. For additional information on the theory
behind the SiteInterlock project, please refer to the accompanying research publication:

- Raschka, Sebastian, Joseph Bemister-Buffington, and Leslie A. Kuhn 2016.
"Detecting the Native Ligand Orientation by Interfacial Rigidity: SiteInterlock."
*Proteins: Structure, Function, and Bioinformatics*
XX (X). John Wiley & Sons : XXX-XX. doi:xx.xxxx/xxxxxxxx. {Manuscript ID: Prot-00209-2016.R1}

# Installation

The `siteinterlock` package is compatible with Python 2.7.x and Python 3.2 or newer;
we recommend using Python 3.5.
The package itself does not require external dependencies or libraries.
If you don't already have Python installed on your system, you can find more information on how to obtain
and install Python at https://www.python.org/downloads/.

To produce the input files that are required for the SiteInterlock analysis,
you will need to have MSU ProFlex installed.
MSU ProFlex (formerly called FIRST) predicts the rigid and flexible regions in a protein structure,
given a Protein Data Bank (PDB) file, which you can process according
to ProFlex instructions to add the necessary
polar hydrogen atom coordinates. You can find more information
about obtaining and installing ProFlex at
http://kuhnlab.bmb.msu.edu/software/proflex/index.html.


## Installing siteinterlock from source

*Please make sure that you are using Python 2.7.x or Python 3.2 or newer
when you are installing and using `siteinterlock`.
You can check the version tag of your Python installation
by executing `python --version` or `python3 --version`
from the command line terminal.*

You can obtain the latest, stable release of `siteinterlock` from GitHub at
https://github.com/psa-lab/siteinterlock/releases


1. After clicking on the `Source code (zip)` or `Source code (tar.gz)`
download links,
please navigate to your download folder and unpack the source code
archive using your preferred archive-tool.

2. Next, go into the unzipped `siteinterlock-master` directory,
and install the `siteinterlock`
package by executing `python setup.py install` (the top level directory in the
`siteinterlock-master` folder).

3. You may verify your installation by opening a new
terminal and executing the following command:
`python -c 'import siteinterlock; print(siteinterlock.__version__)'`,
which should print `1.0.0`. If you receive an

4. Now, you will be able to use the SiteInterlock scripts provided
in the `scripts/` subdirectory from any location on your local drive.

# Documentation

You can find a detailed user guide in the package documentation that
is hosted at
http://psa-lab.github.io/siteinterlock/index.html.

Alternatively, you can view the documentation offline after
downloading `siteinterlock` and opening the `index.html` file that is
located in the `docs/html/` subdirectory in your preferred web browser.

---

---

Copyright (C) 2016 Michigan State University
Developed in the Protein Structural Analysis & Design Laboratory (http://www.kuhnlab.bmb.msu.edu)
Contact Email: kuhnlab@msu.edu
