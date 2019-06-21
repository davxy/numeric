function I = quad_trapezoid(a, b, f, n)
    %
    % Composite quadrature using trapezoid method. 
    %
    % Input
    %   a : integration interval start
    %   b : integration interval end
    %   f : function reference
    %   n : number of segments
    %
    if (b <= a)
        error('interval start must be less than interval stop');
    end
    x = a;
    h = (b - a)/n;
    s = f(a);
    for i = 1 : n-1
        x = x + h;
        s = s + 2*f(x);
    end
    s = s + f(b);
    I = h*s/2;
