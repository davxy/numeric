function yq = spline3(x,y,xq)
    %
    % Cubic Spline interpolation method.
    %
    % Input:
    %   - x  : precomputed points x axis values
    %   - y  : precomputed points y axis values
    %   - xq : query points x axis
    % Output:
    %   - yq : interpolation result for query points
    %
    x = x(:);
    y = y(:);
    [a,b,c,d] = spline_coef(x,y);
    nx = length(x);
    n = length(xq);
    for i=1:length(xq)
        yq(i) = spline_eval(a,b,c,d,x,xq(i));
    end
end


function yq = spline_eval(a,b,c,d,x,xq)
    n = length(x);
    i=1;
    while (i <= n-1 & xq > x(i+1))
        i=i+1;
    end
    % xq is between x(i) and x(i+1)
    yq = a(i)*(xq-x(i))^3 + b(i)*(xq-x(i))^2 + c(i)*(xq-x(i)) + d(i);
end


function T = build_tridiag(h, n)
    % Internal helper function to build the trigiagonal matrix used to find
    % the unknown values m(i)
    for i=1:n
        T(i,i) = 2*(h(i)+h(i+1));
    end
    for i=1:n-1
        T(i+1,i) = h(i);
        T(i,i+1) = h(i+1);
    end
end

function [a,b,c,d] = spline_coef(x,y)
    % Helper function returning a list of coefficients vectors.
    %
    % Input:
	  % - x  : interpolation nodes x axis values
	  % - y  : interpolation nodes y axis values
    % Output:
	  %   - [a,b,c,d] : List of coefficients vectors
    % The polynomial used in the interval [x(i), x(i+1)) is constructed as
    %
	  %   Ci(x) = a[i](x-x[i])^3 + bi(x-x[i])^2 + c[i](x-x[i]) + d[i]
    %
    if (any(size(x) != size(y)))
        error('input x and y vectors must be column vectors of equal length');
    end
    n = length(x);
    % Intervals
    h = x(2:n) - x(1:n-1);
    % Divided differences
    dd = (y(2:n) - y(1:n-1))./h;
    
    % Build the tridiagonal matrix T
    T = build_tridiag(h,n-2);

    % System right hand side
    rhs = 6*(dd(2:end)-dd(1:end-1));
    % Solve the system
    m = T\rhs;
    % Use natural boundary conditions where second derivative
    % is zero at the endpoints
    m = [ 0; m; 0];

    % Get the coefficients
    d = y;
    c = dd - h.*(2*m(1:end-1) + m(2:end))/6;
    b = m/2;
    a = (m(2:end)-m(1:end-1))./(6*h);
end
