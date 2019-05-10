% TEST: linear system with diagonal coefficient matrix

% Matrix main diagonal elements
D = [ 3;5;7;3;1;7;9;10;1;2 ]
% Known terms vector
b = [ 4;8;1;4;3;9;10;12;11;7 ]
% Solve the system
x = diagonal(D, b)
% Check
A = diag(D)
if allclose(b, A*x, 0.1) == 0
    error('Diagonal test failure')
end
