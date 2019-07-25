function I = quad_romberg(a, b, f, n)
    r = quad_romberg_tab(a, b, f, n)
    [m, n] = size(r)
    I = r(m, n)
end

function r = quad_romberg_tab(a, b, f, n)
    %
    % Romberg quadrature
    %
    % Input:
    %   a : integration interval start
    %   b : integration interval end
    %   f : function reference
    %   n : number of rows in Romberg tableau
    % Output:
    %   r : Romberg tableau containing the integral values
    %
    % Examples:
    %   r = romberg(inline('sin(x)'),0,1,5);
    %
    h = (b - a) ./ (2.^(0:n-1));
    r(1,1) = (b - a) * (f(a) + f(b)) / 2;
    for j = 2:n
        subtotal = 0;
        for i = 1:2^(j-2)
            subtotal = subtotal + f(a + (2 * i - 1) * h(j));
        end
        r(j,1) = r(j-1,1) / 2 + h(j) * subtotal;
        for k = 2:j
            r(j,k) = (4^(k-1) * r(j,k-1) - r(j-1,k-1)) / (4^(k-1) - 1);
        end
    end
end
