# Installation

The `siteinterlock` package is compatible with Python 2.6, Python 2.7, and Python 3.x, and it does not require external dependencies or libraries.


## Installing siteinterlock from Source

You can obtain the latest, stable release of `siteinterlock` from GitHub at [https://github.com/rasbt/siteinterlock/releases](https://github.com/rasbt/siteinterlock/releases).

1. After clicking on the `Source code (zip)` or `Source code (tar.gz)` download links, please navigate to your download folder and unpack the source code archive using your preferred archive-tool.
2. Next, go into the unzipped `siteinterlock` directory, and install the siteinterlock package by executing `python setup.py install`.
3. You may verify your installation by executing the following command from your terminal: `python -c 'import siteinterlock; print(siteinterlock.__version__)'`, which should print `1.0.0`.
4. Now, you will be able to use the SiteInterlock scripts provided in the `scripts/` subdirectory from any location on your local drive.
