function A = qr_factor_in(A)
    % QR factorization algorithm working inplace.
    %
    % Returns a matrix with the R factor in the upper right corner
    % and the Householder's vectors in the lower right part.
    % The final Q construction shall be performed by the user.
    %
    % Input:
    %   - A : coefficient matrix.
    % Output:
    %   - A : result matrix.
    m = size(A,1);
    n = size(A,2);
    for i = 1:n
        alpha = norm(A(i:m,i));
        % exit if the matrix does not have rank n
        if alpha == 0
            error('The matrix does not have maximum rank');
        end
        % prevent numerical cancellation
        if A(i,i) >= 0
            alpha = -alpha;
        end
        v1 = A(i,i) - alpha;
        A(i,i) = alpha;
        A(i+1:m,i) = A(i+1:m,i)/v1;
        % beta = (alpha-z1)/alpha = 2/(u'u)
        %   with u the scaled Householder's vector u=(z-alpha*ei)/(z1-alpha*e1)
        beta = -v1/alpha;
        A(i:m,i+1:n) = A(i:m,i+1:n) - (beta*[1; A(i+1:m,i)]) * ...
                        ([1 A(i+1:m,i)'] * A(i:m,i+1:n));
    end
end
