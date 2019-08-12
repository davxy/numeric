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
        L(i, i) = sqrt(A(i, i) - L(i, :)*L(i, :)');
        for j = (i+1):n
            L(j, i) = (A(j, i) - L(i, :)*L(j, :)') / L(i, i);
        end
    end
end
