# Mebuex
A setuptools `Extension` and `build_ext` wrapper for builds based on Meson.

## Usage
Mebuex assumes that the structure of a package is as follows:
```
root
 | - builddir
 | ... some source layout to be compiled with Meson ...
 | - *packagename*
 |    | ... Python package layout handled by setup.py ...
 | - setup.py
 | - meson.build
```
That is, the root directory of the package contains the `setup.py` file,
the `meson.build` file, a Meson build directory (here `builddir`, but can be
configured), directories covering the sources to be built by Meson, and the
Python package source tree.

The relevant part of this layout is that `setup.py` and `meson.build` are
contained in the root directory, and that a designated build directory is
specified (need not exist before building). The Meson build file should contain
all relevant configuration to build a Python extension within the build
directory (here `builddir`). The `setup.py` file should be based on setuptools
and contain all relevant configuration for the Python part of the package.

Within the `setup.py` file, the Python extension built by Meson can then be
included using the `MesonExtension` and `build_ext` commands supplied by Mebuex.
An example code would look like this (suppose that the Meson build would yield
an extension `mypackage.backend`):
```python
from setuptools import setup
from mebuex import MesonExtension, build_ext

ext = MesonExtension('mypackage.backend', builddir='builddir')

setup(name='mypackage',
      version='1.0.0',
      author='Me',
      description='Or is it yours?',
      ext_modules=[ext],
      cmdclass={'build_ext' : build_ext}
)
```

## Install
Mebuex can be installed with Pip:
```bash
pip install .
```

## License
Mebuex is licensed under the MIT license (see the LICENSE file).

## Changelog
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### [1.1.0] - 2022-07-13
#### Changed
 - Fixed empty lib being copied to wheel directory instead of Meson-compiled
   lib.
 - Fix handling of dots in compiled names (likely irrelevant).

### [1.0.0] - 2022-07-13
#### Added
 - First version
