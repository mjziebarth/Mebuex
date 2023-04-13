/*
 * A Mebuex example project: C++ source file.
 *
 * Author: Malte J. Ziebarth (mjz.science@fmvkb.de)
 *
 * Copyright 2023, Malte J. Ziebarth
 * SPDX-License-Identifier: MIT
 */

#include <fancynumerics.hpp>
#include <cmath>

using mebuexexample::FancyNumerics;

/*
 * Construct a fancy numerics:
 */
FancyNumerics::FancyNumerics(double a, double b, double c)
   : a(a), b(b), c(c)
{
}


/*
 * Perform fancy numerics:
 */
double FancyNumerics::compute(double x) const
{
	return a * (x - b) * std::exp(-x / c);
}
