function Y = least_squares(x, y, d, X)
    % Least squares polynomial
    %
    % Input:
    %   - x : x-axis known values
    %   - y : y-axis known values
    %   - d : degree of polynomial you want to use
    %   - X : query points x axis
    % Output:
    %   - Y : values of the least squares polynomial at the query points
    x = x(:);
    y = y(:);
    n = d + 1;
    % Build the Vandermonde matrix
    A = ones(length(x), n);
    for i = 2:n
        A(:,i) = x .* A(:,i-1);
    end
    % QR factorization
    [ Q R ] = qr_factor(A);
    % Least squares vector is vector z such that T*z = g1
    g = Q' * y;
    g1 = g(1:n);
    T = R(1:n,1:n);
    z = triangular(T, g1, 0);
    % Evaluation of polynomial at query points
    Y = polyval(fliplr(z'), X);
end
