% TEST: LU factorization

% Non-singular 6x6 matrix
A = [ 29 11 59  9 13;
      41 27  3 13  1;
      53 62 23 13 50;
      61 61 54 40 29;
      49 27  0 18 62 ]
% inplace computation of LU matrices
B = lu_factor(A)
% extract lower part
L = tril(B,-1) + eye(5)
% extract upper part
U = triu(B)
% Check
if allclose(A, L*U, 0.1) == 0
    error('LU factorizzation test failure')
end

% TEST: System Resolution

% Ax = LUx = b
b = [ 68; 9; 45; 43; 35 ]
% Lk = b 
k = triangular(L, b, 1)
% Ux = k
x = triangular(U, k, 0)
% Check
b1 = A*x
if allclose(b, b1, 0.1) == 0
    error('System resolution failure')
end
