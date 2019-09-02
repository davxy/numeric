function Y = lagrange(x, y, X)
    %
    % Lagrange interpolation method.
    %
    % Input:
    %   - x : precomputed points x axis values
    %   - y : precomputed points y axis values
    %   - X : query points x axis
    % Output:
    %   - Y : query points y axis (interpolation results)
    %
    if (size(x,2) != size(y,2))
        error('x and y must have the same number of elements')
    end
    n = size(x, 2);
    Y = zeros(1, size(X, 2));
    for i = 1:n
        L = ones(1, size(X,2));
        for j = 1:n
            if (i != j)
                L = L .* (X-x(j))/(x(i)-x(j));
            end
        end
        Y = Y + y(i)*L;
   end
end
