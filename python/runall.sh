#!/bin/bash
# Run all the tests and experiments.
# Used for debugging purposes only.

RUN=python3

# Numerical cancellation
$RUN epsilon.py
$RUN cancel.py

# Root finding
$RUN bisect_test.py
$RUN newton_test.py
$RUN bisect_fallback.py

# Linear systems
$RUN orthogonal_test.py
$RUN diagonal_test.py
$RUN triangular_test.py
$RUN lu_factor_test.py
$RUN palu_factor_test.py
$RUN qr_factor_test.py
$RUN rref_test.py

# Misc
$RUN divdiff_test.py
$RUN vander_test.py

# Interpolation
$RUN lagrange_test.py
$RUN spline1_test.py
$RUN spline3_test.py
$RUN least_squares_test.py
$RUN chebyshev_poly.py
$RUN chebyshev_poly2.py
$RUN runge_test.py
$RUN lebesgue.py

# Misc
$RUN toom3.py

# Differentiation
$RUN diff_ffd_test.py
$RUN diff_sdq_test.py
$RUN diff_err.py
