# SiteInterlock

<div style="max-width:50%;">
<img src="docs/sources/images/logo_small.png" alt="SiteInterlock Logo">
</div>

![Python 2.6](https://img.shields.io/badge/python-2.6-blue.svg)
![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3](https://img.shields.io/badge/python-3-blue.svg)
[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](/license/index.html)



***A novel approach to pose selection in protein-ligand docking based on graph theory.***

`siteinterlock` is a Python package for selecting near-native protein-ligand docking poses based on the hypothesis that interfacial rigidification of both the protein and ligand prove to be important characteristics of the native binding mode and are sensitive to the spatial coupling of interactions and bond-rotational degrees of freedom in the interface.

The `siteinterlock` package was developed in the [Protein Structure Analysis & Design Laboratory](http://www.kuhnlab.bmb.msu.edu) at Michigan State University. For additional information on the theory behind the SiteInterlock project, please refer to the accompanying research publication:

- Raschka, Sebastian, Joseph Bemister-Buffington, and Leslie A. Kuhn 2016. "Detecting the Native Ligand Orientation by Interfacial Rigidity: SiteInterlock." *Proteins: Structure, Function, and Bioinformatics* XX (X). John Wiley & Sons : XXX-XX. doi:xx.xxxx/xxxxxxxx.
 {insert link to publisher website}

# Installation

The `siteinterlock` package is compatible with Python 2.6, Python 2.7, and Python 3.x, and it does not require external dependencies or libraries.


## Installing siteinterlock from Source

You can obtain the latest, stable release of `siteinterlock` from GitHub at [https://github.com/rasbt/siteinterlock/releases](https://github.com/rasbt/siteinterlock/releases).

1. After clicking on the `Source code (zip)` or `Source code (tar.gz)` download links, please navigate to your download folder and unpack the source code archive using your preferred archive-tool.
2. Next, go into the unzipped `siteinterlock` directory, and install the `siteinterlock` package by executing `python setup.py install`.
3. You may verify your installation by executing the following command from your terminal: `python -c 'import siteinterlock; print(siteinterlock.__version__)'`, which should print `1.0.0`.
4. Now, you will be able to use the SiteInterlock scripts provided in the `scripts/` subdirectory from any location on your local drive.


# Documentation

You can find a detailed user guide in the package documentation that is hosted at http://psa-lab.github.io/siteinterlock/index.html

Alternatively, you can view the documentation offline after downloading `siteinterlock` and opening the index.html file that is located in the `docs/html/` subdirectory by opening it in your preferred web browser.
