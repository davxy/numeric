% PA=LU factoriazation algorithm
%
% input:
%   - A : the coefficient matrix
% output:
%   - A : the LU factorized matrix
%   - p: permutation vector
%
function [A,p] = palu_factor(A)
    n = length(A);
    % permutation indexes vector initialization
    p = 1:n;
    for i = 1:n-1
        [maxval,row] = max(abs(A(i:n,i)));
        % align vector row with matrix row
        row = row+i-1;
        % for each iteration check that maxval is non-zero
        if maxval == 0
            error('The matrix is singular');
        end
        if row > i
            % rows swap
            A([i,row],:) = A([row,i],:);
            % update the permutation vector
            p([i,row]) = p([row,i]);
        end
        % computation of the i-th Gauss vector that will be part of the L matrix
        A(i+1:n,i) = A(i+1:n,i)/A(i,i);
        % recomputation of the square sub-matrix defined under the i-th row and
        % after the i-th column
        A(i+1:n,i+1:n) = A(i+1:n,i+1:n) - A(i+1:n,i)*A(i,i+1:n);
    end
end
