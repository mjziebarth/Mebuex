# A Mebuex example project: Setuptools setup.py file.
#
# Author: Malte J. Ziebarth (mjz.science@fmvkb.de)
#
# Copyright 2023, Malte J. Ziebarth
# SPDX-License-Identifier: MIT

from setuptools import setup
from mebuex import MesonExtension, build_ext

ext = MesonExtension('mebuexexample.fancynumerics', builddir='builddir')

setup(ext_modules=[ext], cmdclass={'build_ext' : build_ext})
