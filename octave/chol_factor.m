function L = chol_factor(A)
    %
    % Cholesky LL' factorization
    %
    % Input
    %   A : input matrix
    % Output
    %   L : lower triangular matrix factor (A=L*L')
    %
    n = length(A);
    L = zeros(n, n);
    for i = 1:n
        val = A(i, i) - L(i, :)*L(i, :)';
        if val < 0
            error('The matrix is not positive definite');
        end
        L(i, i) = sqrt(val);
        for j = (i+1):n
            L(j, i) = (A(j, i) - L(i, :)*L(j, :)') / L(i, i);
        end
    end
end
