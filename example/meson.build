# A Mebuex example project: Meson build file.
#
# Author: Malte J. Ziebarth (mjz.science@fmvkb.de)
#
# Copyright 2023, Malte J. Ziebarth
# SPDX-License-Identifier: MIT

project('mebuexexample','cpp','cython')

libfancynumerics = static_library(
    'fancynumerics', ['src/fancynumerics.cpp'],
    include_directories : include_directories('include')
)


python = import('python').find_installation()
dep_py = python.dependency()

python.extension_module('fancynumerics',
                        'mebuexexample/fancynumerics.pyx',
                        dependencies : [dep_py],
                        include_directories : include_directories('include'),
                        override_options : ['cython_language=cpp'],
                        link_with : libfancynumerics)