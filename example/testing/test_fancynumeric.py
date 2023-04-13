# A Mebuex example project: Pytest file.
#
# Author: Malte J. Ziebarth (mjz.science@fmvkb.de)
#
# Copyright 2023, Malte J. Ziebarth
# SPDX-License-Identifier: MIT

import numpy as np
from mebuexexample import FancyNumerics

def test_fancynumerics():
    # Test numerics:
    a = 2.5
    b = 1.0
    c = 10.5
    fn = FancyNumerics(a,b,c)

    # Test point:
    x = np.atleast_1d(7.7)
    y0 = fn.compute(x)
    y1 = a * (x - b) * np.exp(-x/c)

    assert np.allclose(y0,y1)
