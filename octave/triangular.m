%
% Triangular matrix resolution method
%
% input:
%  - A: triangular matrix
%  - b: known terms vector
%  - type: 0 if A is upper triangular, 1 if is lower triangular
% output:
%  - x: the results vector
%
function x = triangular(A, b, type)
  n = length(b);
  if type == 1
    start = 1;
    stop  = n;
    step  = 1;
  else
    start = n;
    stop  = 1;
    step  = -1;
  end
  for i=start:step:stop
    x(i) = b(i);
    for j=start:step:i-step
      x(i) = x(i)-A(i,j)*x(j);
    end
    x(i) = x(i)/A(i,i);
  end
  x = x'; % return a column vector 
  return
end

