/*
 * A Mebuex example project: C++ header file.
 *
 * Author: Malte J. Ziebarth (mjz.science@fmvkb.de)
 *
 * Copyright 2023, Malte J. Ziebarth
 * SPDX-License-Identifier: MIT
 */

#ifndef FANCYNUMERICS_HPP
#define FANCYNUMERICS_HPP

namespace mebuexexample {

class FancyNumerics {
public:
	FancyNumerics(double a, double b, double c);

	double compute(double x) const;

private:
	const double a;
	const double b;
	const double c;
};

}

#endif