% TEST: linear system with triangular coefficient matrix

% Lower triangular test
A = [ 12  0  0  0  0;
      18 38  0  0  0;
      51  4 57  0  0;
      53  3  8  2  0;
      31 26  4 16 60 ]
% Known terms vector
b = [ 68; 9; 45; 43; 35 ]
% Solve the system
x = triangular(A, b, 1)
% Check
if allclose(b, A*x, 0.1) == 0
    error('Lower triangular test failure')
end

% Upper triangular test
A = [ 12 48  2 51 49;
       0 38 32 51  5;
       0  0 57  2 31;
       0  0  0  2 53;
       0  0  0  0 60 ]
% Known terms vector
b = [ 7; 31; 32; 34; 22 ]
% Solve the system
x = triangular(A, b, 0)
% Check
if allclose(b, A*x, 0.1) == 0
    error('Upper triangular test failure')
end

