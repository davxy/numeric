%
% Diagonal sistem solver
%
% input:
%  - D: vector with matrix diagonal elements
%  - b: known terms vector
% output:
%  - x: the results vector
%
function x = diagonal(D, b)
    dlen = length(D);
    if dlen != length(b)
       error('Error: input vectors length mismatch');
    end
    for i=1:dlen
        x(i) = b(i)/D(i);
    end
    x = x'; % return a column vector
end
