function Y = newton_interp(x, y, X)
    %
    % Newton interpolation method.
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
    Y = zeros(1,size(X, 2));
    for k = 1:n
        L = ones(1, size(X, 2));
        for i = 1:(k-1)
            L = L .* (X - x(i));
        end
        a = divdiff(x(1:k), y(1:k));
        Y = Y + a*L;
    end
end
