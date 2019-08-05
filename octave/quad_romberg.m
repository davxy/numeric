function I = quad_romberg(a, b, f, n)
    %
    % Romberg quadrature
    %
    % Input:
    %   a : integration interval start
    %   b : integration interval end
    %   f : function reference
    %   n : number of rows in Romberg tableau
    % Output:
    %   I : Romberg table most accurate value (I(nn))
    %
    r = quad_romberg_tab(a, b, f, n);
    I = r(n, n);
end

function r = quad_romberg_tab(a, b, f, n)
    %
    % Romberg integral table
    %
    % Input:
    %   a : integration interval start
    %   b : integration interval end
    %   f : function reference
    %   n : number of rows in Romberg tableau
    % Output:
    %   r : Romberg table containing the integral values
    %
    h = (b - a) ./ (2.^(0:n-1));
    r(1,1) = (b - a) * (f(a) + f(b)) / 2;
    for i = 2:n
        subtotal = 0;
        for k = 1:2^(i-2)
            subtotal = subtotal + f(a + (2*k - 1)*h(i));
        end
        r(i,1) = r(i-1,1) / 2 + h(i) * subtotal;
        for k = 2:i
            r(i,k) = (4^(k-1) * r(i,k-1) - r(i-1,k-1)) / (4^(k-1) - 1);
        end
    end
end
