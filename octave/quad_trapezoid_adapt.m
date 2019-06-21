function [ I x ] = quad_trapezoid_adapt(a, b, f, tol)
    %
    % Composite quadrature using adaptive trapezoid method.
    %
    % Input
    %   a : integration interval start
    %   b : integration interval end
    %   f : function reference
    %   tol: tolerance
    % Output
    %   I : integral estimation
    %   x : x nodes
    %
    I1 = quad_trapezoid(a, b, f, 1);
    I2 = quad_trapezoid(a, b, f, 2);
    e = abs(I1-I2)/3;
    if (e <= tol)
        I = I2;
        x = [ a, (a+b)/2, b ];
    else
        [ I1 x1 ] = quad_trapezoid_adapt(a, (a+b)/2, f, tol/2);
        [ I2 x2 ] = quad_trapezoid_adapt((a+b)/2, b, f, tol/2);
        I = I1 + I2;
        x = union(x1, x2);
    end
end
