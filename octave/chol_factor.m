function L = chol_factor(M)
    %
    % Cholesky LL' factorization
    %
    % Input
    %   M : input matrix
    % Output
    %   L : lower triangular matrix factor (M=L*L')
    %
    n = length(M);
    L = zeros(n, n);
    for i = 1:n
        %L(i, i) = sqrt(M(i, i) - L(i, :)*L(i, :)');
        L(i, i) = sqrt(M(i, i) - L(i, 1:i-1)*L(i, 1:i-1)');
        for j = (i+1):n
            L(j, i) = (M(j, i) - L(i, :)*L(j, :)') / L(i, i);
        end
    end
end
