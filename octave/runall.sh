#!/bin/bash

# Octave runner
RUN=octave
# Matlab runner
#RUN=matlab

# Root finding
$RUN bisect_test.m
$RUN newton_test.m
$RUN bisect_fallback.m

# Linear systems
$RUN orthogonal_test.m
$RUN diagonal_test.m
$RUN triangular_test.m
$RUN lu_factor_test.m
$RUN palu_factor_test.m
$RUN qr_factor_test.m
$RUN rref_test.m

# Misc
$RUN divdiff_test.m
$RUN vander_test.m

# Interpolation
$RUN lagrange_test.m
$RUN spline3_test.m
$RUN least_squares_test.m
