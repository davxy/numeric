function I = quad_simpson(a, b, f, n)
    %
    % Composite quadrature using 1/3 Simpson's method. 
    %
    % Input
    %   a : integration interval start
    %   b : integration interval end
    %   f : function reference
    %   n : number of segments
    % Output
    %   I : integral estimation
    %
    if (b <= a)
        error('interval start must be less than interval stop');
    end
    x = a;
    h = (b - a)/n;
    s = f(x) + 4*f(x+h/2);
    for i = 1 : n-1
        x = x + h;
        s = s + 2*f(x) + 4*f(x+h/2);
    end
    s = s + f(b);
    I = h*s/6;
end
