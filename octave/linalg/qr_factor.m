function [ Q R ] = qr_factor(A)
    % QR factorization algorithm
    %
    % Input:
    %   - A : coefficient matrix
    % Output:
    %   - Q : first factor
    %   - R : second factor
    R = qr_factor_in(A);
    m = size(R,1);
    n = size(R,2);
    Q = eye(m);
    for i = 1:n
        v = [1; R(i+1:m,i)];
        H = eye(m);
        H(i:m,i:m) = eye(m-i+1) - 2*(v*v')/(v'*v);
        Q = Q*H;
        R(i+1:m,i) = zeros(m-i,1);
    end
end
