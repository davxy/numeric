% TEST: linear system with orthogonal coefficient matrix

% 2x2 orthogonal matrix
A = [ 1  1;
      1 -1 ];
A = A*1.0/sqrt(2.0)
% Known terms vector
b = [ 2; 3 ]
% Solve the system (skip orthogonality check)
x = orthogonal(A, b, 0)
% Check
if allclose(b, A*x, 0.0001) == 0
    error('Orthogonal test failure')
end

% 3x3 orthogonal matrix
A = [ 2 -2  1;
      1  2  2;
      2  1 -2 ];
A = A*1.0/3.0
% Known terms vector
b = [ 2; 3; 4 ]
% Solve the system (with orthogonality check)
x = orthogonal(A, b, 1)
% Check
if allclose(b, A*x, eps) == 0
    error('Error: orthogonal test failure')
end
