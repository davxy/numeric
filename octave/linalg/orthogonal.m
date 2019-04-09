%
% Orthogonal matrix resolution methof
%
% Input:
%   - A: orthogonal matrix
%   - b: known terms vector
%   - check: check for orthogonality
function x = orthogonal(A, b, chk)
    if chk == 1 && is_orthogonal(A) == 0
        error('Not orthogonal input matrix')
    end
    x = transpose(A) * b
end

%
% Check if a matrix is orthogonal
%
function b = is_orthogonal(A)
    b = allclose(A*transpose(A), eye(size(A,1)), 0.001)
end
