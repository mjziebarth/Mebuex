# A Mebuex example project: Cython file.
#
# Author: Malte J. Ziebarth (mjz.science@fmvkb.de)
#
# Copyright 2023, Malte J. Ziebarth
# SPDX-License-Identifier: MIT

import numpy as np
from libcpp.memory cimport shared_ptr, make_shared
from cython.operator cimport dereference as deref

cdef extern from "fancynumerics.hpp" namespace "mebuexexample" nogil:
    cdef cppclass FancyNumerics:
        FancyNumerics(double a, double b, double c) except+
        double compute(double x) const

cdef class CyFancyNumerics:
    """
    A test class doing fancy numerics.
    """
    cdef shared_ptr[FancyNumerics] _numerics

    def __init__(self, double a, double b, double c):
        self._numerics = make_shared[FancyNumerics](a, b, c)

    def compute(self, const double[:] x):
        cdef size_t i, N
        N = x.shape[0]
        cdef double[::1] result = np.empty(N)
        with nogil:
            for i in range(N):
                result[i] = deref(self._numerics).compute(x[i])

        return result.base
