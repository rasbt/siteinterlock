# Installation

The `siteinterlock` package is compatible with Python 2.7.x and Python 3.x; the package itself does not require external
dependencies or libraries. If you don't already have Python installed on your system, you can find more information on how to obtain
and install Python at [https://www.python.org/downloads/](https://www.python.org/downloads/).

To produce the input files that are required for the SiteInterlock analysis, you will need to have [MSU ProFlex installed](http://kuhnlab.bmb.msu.edu/software/index.html)<sup> 1</sup>. MSU ProFlex (formerly called FIRST) predicts the rigid and flexible regions in a protein structure, given a Protein Data Bank (PDB) file, including polar hydrogen atoms. You can find more information about obtaining and installing ProFlex at [http://kuhnlab.bmb.msu.edu/software/proflex/index.html](http://kuhnlab.bmb.msu.edu/software/proflex/index.html).


## Installing siteinterlock from source

You can obtain the latest, stable release of `siteinterlock` from GitHub at [https://github.com/psa-lab/siteinterlock/releases](https://github.com/psa-lab/siteinterlock/releases).

1. After clicking on the `Source code (zip)` or `Source code (tar.gz)` download links, please navigate to your download folder and unpack the source code archive using your preferred archive-tool.
2. Next, go into the unzipped `siteinterlock-master` directory, and install the `siteinterlock` package by executing `python setup.py install` (inside `siteinterlock-master`).
3. You may verify your installation by opening a new terminal and executing the following command: `python -c 'import siteinterlock; print(siteinterlock.__version__)'`, which should print `1.0.0`.
4. Now, you will be able to use the SiteInterlock scripts provided in the `scripts/` subdirectory from any location on your local drive.

---

<sup>1 </sup>Jacobs, D. J., Rader, A. J., Kuhn, L. A., & Thorpe, M. F. (2001). Protein flexibility predictions using graph theory. *Proteins: Structure, Function, and Bioinformatics*, 44(2), 150-165.
