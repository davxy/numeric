function Y = spline3(x, y, X)
    %
    % Cubic Spline interpolation method.
    %
    % Input:
    %   - x : precomputed points x axis values
    %   - y : precomputed points y axis values
    %   - X : query points x axis
    % Output:
    %   - Y : query points y axis (interpolation results)
    %
    x = x(:);
    y = y(:);
    [a, b, c, d] = spline3_coef(x, y);
    for i = 1:length(X)
        Y(i) = spline3_eval(a, b, c, d, x, X(i));
    end
end


function Yi = spline3_eval(a, b, c, d, x, Xi)
    %
    % Evaluation function.
    %
    % Input:
    %   - [ a, b, c, d ] : spline coefficients list 
    %   - x  : precomputed points x axis values
    %   - Xi : query point
    % Output:
    %   - Yi : spline value at query point
    %
    i=1;
    while (i <= length(x)-1 & Xi > x(i+1))
        i=i+1;
    end
    % Xi is between x(i) and x(i+1)
    Yi = a(i)*(Xi-x(i))^3 + b(i)*(Xi-x(i))^2 + c(i)*(Xi-x(i)) + d(i);
end


function T = build_tridiag(h, n)
    %
    % Internal helper function to build the trigiagonal matrix used to find
    % the unknown values m(i)
    %
    for i = 1:n
        T(i, i) = 2*(h(i) + h(i+1));
    end
    for i = 1:n-1
        T(i+1, i) = h(i+1);
        T(i, i+1) = h(i+1);
    end
end

function [a, b, c, d] = spline3_coef(x, y)
    %
    % Helper function returning a list of coefficients vectors.
    % Assumption: x and y shall be of the same length
    %
    % Input:
	%   - x : interpolation nodes x axis values
	%   - y : interpolation nodes y axis values
    % Output:
	%   - [a,b,c,d] : List of coefficients vectors
    %     The polynomial used in the interval [x(i), x(i+1)) is constructed as
	%     Ci(x) = a[i](x-x[i])^3 + bi(x-x[i])^2 + c[i](x-x[i]) + d[i]
    %
    n = length(x);
    % Intervals lengths
    h = x(2:n) - x(1:n-1);
    % Divided differences
    dd = (y(2:n) - y(1:n-1))./h;
    % Build the tridiagonal matrix T
    T = build_tridiag(h,n-2);
    % System right hand side and solve the system
    rhs = 6*(dd(2:end)-dd(1:end-1));
    m = T\rhs;
    % Natural boundary conditions: second derivative is zero at the endpoints
    m = [ 0; m; 0];
    % Get the coefficients
    d = y;
    c = dd - h.*(2*m(1:end-1) + m(2:end))/6;
    b = m/2;
    a = (m(2:end)-m(1:end-1))./(6*h);
end
