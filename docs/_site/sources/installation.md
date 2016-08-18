# Installation

The `siteinterlock` package is compatible with both Python 2.7 and Python 3.x and does not require external dependencies or libraries. Below, you can find If you are using `pip`, you can download and install


## Installing from Source

You can obtain the latest, stable release of `siteinterlock` from GitHub at [https://github.com/rasbt/siteinterlock/releases](https://github.com/rasbt/siteinterlock/releases).

1. After clicking on the `Source code (zip)` or `Source code (tar.gz)` download links, go to your download folder and unpack the source code archive using your preferred archive-tool.
2. Next, go into the unzipped `siteinterlock` directory, and install the siteinterlock package by executing `python setup.py install`.
3. You may verify your installation by executing the following command from your terminal: `python -c 'import siteinterlock; print(siteinterlock.__version__)'`, which should print `1.0.0`.
4. Now, you will be able to use the SiteInterlock scripts provided in the `scripts/` subdirectory from any location on your local drive.


## Installing from PyPI via pip

If you are using `pip`, you can download and install SiteInterlock directly from [PyPI](https://pypi.python.org/pypi), the Python Package Index, by executing

```bash
pip install siteinterlock  
```

{!!add note about the scripts directory}

### Upgrading via pip

To upgrade an existing version of `siteinterlock` from PyPI, execute

```bash
pip install siteinterlock --upgrade
```
