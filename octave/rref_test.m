% Reduced Row Echelon Form test using both builtin function (rref) and our
% implementation

A = [  1, 2, -1, -4;
       2, 3, -1, -11;
      -2, 0, -3,  22 ];

refA = rref(A);
disp(refA);
