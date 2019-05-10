% TEST: PA=LU Factorization

% factorization of a 6x6 matrix that is not LU factorizable
A = [ 0  41 53 12 62 26;
      43 49 61 60 22 27;
      65 25 56 38 43 43;
      37  0 24 42 26 56;
      26 28 41 15 42 24;
      13 50 48 36 46 28 ]
% LU factorization
[B,p] = palu_factor(A);
% Extract lower part
L = tril(B,-1) + eye(6)
% Extract upper part
U = triu(B)
% Check
LU = L*U
if allclose(A(p,:), LU, 0.1) == 0
    error('LU factorizzation test failure')
end

% TEST: System Resolution
% Ax = b => PAx = Pb => LUx = Pb
% LUx = Pb
b = [ 33; 35; 2; 49; 53; 21 ]
% Lk = Pb  (note the permutation of b using the index vector p)
k = triangular(L, b(p), 1)
% Ux = k
x = triangular(U, k, 0)
% Check
if allclose(b, A*x, 0.1) == 0
    error('Lower triangular test failure')
end
