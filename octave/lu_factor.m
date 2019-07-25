function A = lu_factor(A)
    % LU factorization algorithm
    %
    % Input:
    %   - A : the coefficient matrix
    % Output:
    %   - A : the LU factorized matrix
    n = length(A);
    for i = 1:n-1
        % exit if at the i-th step the diagonal element is 0
        if A(i,i) == 0
            error('The matrix is not LU factorizable');
        end
        % computation of the i-th Gauss vector that will be part of the L matrix 
        A(i+1:n,i) = A(i+1:n,i)/A(i,i);
        % recomputation of the square sub-matrix defined under the i-th row and
        % after the i-th column
        A(i+1:n,i+1:n) = A(i+1:n,i+1:n) - A(i+1:n,i)*A(i,i+1:n);
    end
end
