function D = divdiff(x, y)
    %
    % Divided differences computation using recursion
    %
    % Input:
    %   - x : points x axis
    %   - y : points y axis
    % Output:
    %   - D : divided differences
    %
    n = length(x);
    if n == 1
        D = y(1);
    else
        D = (divdiff(x(2:n),y(2:n)) - divdiff(x(1:n-1),y(1:n-1))) / (x(n)-x(1));
    end
end

