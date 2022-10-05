# A setuptools build_ext hack to use the Meson build system.
#
# Author: Malte J. Ziebarth (mjz.science@fmvkb.de)
#
# Copyright 2022, Malte J. Ziebarth and the setuptools contributors
# SPDX-License-Identifier: MIT

import os
import subprocess
from pathlib import Path
from setuptools.command.build_ext import build_ext as build_ext_st
from distutils.file_util import copy_file
from .extension import MesonExtension

class build_ext(build_ext_st):
    """
    `build_ext` command to build Meson-based builds.
    """
    def build_extension(self, ext):
        if isinstance(ext, MesonExtension):
            # Meson build.
            # First ensure that the build directory is set up:
            currentpath = Path().resolve()
            buildpath = (Path(ext.sourcepath) / ext.builddir).resolve()
            if not Path(buildpath).is_dir():
                os.chdir(ext.sourcepath)
                subprocess.run(["meson","setup",ext.builddir], check=True)

            # Compile within the build directory:
            os.chdir(buildpath)
            subprocess.run(["meson","compile"], check=True)
            os.chdir(currentpath)

            # Copy the file.
            #
            # This following code to compute the relevant path and file names,
            # is, up to the comment marking the end, adapted from
            # setuptools/command/build_ext.py, released under MIT license.
            #
            # The license conditions of setuptools follows:
            #
            # Copyright Jason R. Coombs
            #
            # Permission is hereby granted, free of charge, to any person
            # obtaining a copy of this software and associated documentation
            # files (the "Software"), to deal in the Software without
            # restriction, including without limitation the rights to use, copy,
            # modify, merge, publish, distribute, sublicense, and/or sell copies
            # of the Software, and to permit persons to whom the Software is
            # furnished to do so, subject to the following conditions:
            #
            # The above copyright notice and this permission notice shall be
            # included in all copies or substantial portions of the Software.
            #
            # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
            # EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
            # OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
            # NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
            # HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
            # WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
            # FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
            # OTHER DEALINGS IN THE SOFTWARE.
            #
            cmd = self.get_finalized_command('build_py')
            fullname = self.get_ext_fullname(ext.name)
            pdir = cmd.get_package_dir('.'.join(fullname.split('.')[:-1]))
            modname = ext.compiledname.split('.')[-1]
            filename = ext.compiledname + self.get_ext_filename(fullname) \
                                              .split(modname)[-1]
            destpath = Path(cmd.build_lib) / pdir
            if not destpath.is_dir():
                raise RuntimeError("Cannot copy built extension because the "
                                   "target directory does not exist. This "
                                   "likely indicates a missing sub-package in "
                                   "the setup configuration.")
            destname = (destpath / filename).resolve()
            copy_file((Path(buildpath) / filename).resolve(),
                      destname, verbose=self.verbose,
                dry_run=self.dry_run
            )
            # end of adapted code from setuptools/command/build_ext.py.
        else:
            # Normal build.
            super().build_extension(ext)
