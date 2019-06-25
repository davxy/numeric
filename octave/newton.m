function [x, steps] = newton(x, f, f1, tolx, imax, m)
    %
    % Newton root finding method
    %
    % Input:
    %   - x    : first root approximation
    %   - f    : function reference
    %   - f1   : first derivative function reference
    %   - tolx : max tolerance
    %   - imax : max iterations before stop trying
    %   - m    : root multiplicity; if unknown set to 1.
    % Output:
    %   - x     : final root approximation
    %   - steps : required steps
    %
    for i = 1:imax
        fx = f(x);
        f1x = f1(x);
        if (abs(fx) <= tolx*abs(f1x))
            break;
        end
        x = x - m*(fx/f1x);
    end
    steps = i;
end
