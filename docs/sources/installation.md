# Installation

The `siteinterlock` package is compatible with current versions of Python such as Python 3.2 or newer, and the package itself does not require external dependencies or libraries. You can find more information on how to obtain and install Python at https://www.python.org/downloads/.

To produce the input files that are required for the SiteInterlock analysis, you will need to have MSU ProFlex installed. MSU ProFlex (formerly called FIRST) predicts the rigid and flexible regions in a protein structure, given a Protein Data Bank (PDB) file including polar hydrogen atoms. You can find more information about obtaining and installing ProFlex at http://kuhnlab.bmb.msu.edu/software/index.html.


## Installing siteinterlock from Source

You can obtain the latest, stable release of `siteinterlock` from GitHub at [https://github.com/rasbt/siteinterlock/releases](https://github.com/rasbt/siteinterlock/releases).

1. After clicking on the `Source code (zip)` or `Source code (tar.gz)` download links, please navigate to your download folder and unpack the source code archive using your preferred archive-tool.
2. Next, go into the unzipped `siteinterlock` directory, and install the `siteinterlock` package by executing `python setup.py install`.
3. You may verify your installation by executing the following command from your terminal: `python -c 'import siteinterlock; print(siteinterlock.__version__)'`, which should print `1.0.0`.
4. Now, you will be able to use the SiteInterlock scripts provided in the `scripts/` subdirectory from any location on your local drive.
