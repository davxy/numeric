% TEST: Cholesky factorization (LL')

% Symmetric positive definite matrix
A = [ 5    1.2  0.3 -0.6;
      1.2  6   -0.4  0.9;
      0.3 -0.4  8    1.7;
     -0.6  0.9  1.7  10 ]
% Computation of the L factor
L = chol_factor(A)
% Check
if allclose(A, L*L', 0.0001) == 0
    error('Cholesky factorization test failure')
end

% TEST: System Resolution

% Ax = LL'x = b
b = [ 68; 9; 45; 35 ]
% Lk = b
k = triangular(L, b, 1)
% L'x = k
x = triangular(L', k, 0)
% Check
b1 = A*x
if allclose(b, b1, 0.0001) == 0
    error('System resolution failure')
end
