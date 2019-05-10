%--------------------------------------
% TEST: QR factorization
%--------------------------------------
printf('\nTEST: QR factorization\n\n');
% Overdetermined matrix
A = [ -1 -1  1;
       1  3  3;
      -1 -1  5;
       1  3  7 ]
% QR factorization
[ Q, R ] = qr_factor(A)
% Results check
if allclose(A, Q*R, 0.0001) == 0
    error('QR factorizzation test failure')
end

%--------------------------------------
% TEST: least squares solution
%--------------------------------------
printf('\nTEST: least squares solution\n\n');
% Overdetermined cohefficient matrix
A = [ 3 2 1;
      1 2 3;
      1 2 1;
      2 1 2 ]
% known values vector
b = [ 10; 10; 10; 10 ]
% QR factorization
[ Q, R ] = qr_factor(A);
% Results check
if allclose(A, Q*R, 0.0001) == 0
    error('QR factorizzation test failure')
end
n = size(R,2);
g = Q'*b;
g1 = g(1:n);
T = R(1:n,1:n);
% Solve the upper triangular system Tx=g1
x = triangular(T, g1, 0)
% Result remainder
r = A*x - b