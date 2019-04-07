function [x,steps] = bisect(a,b,f,tolx)
    %
    % Bisection root finding method
    %
    % Input:
    %   - a : confidence interval start
    %   - b : confidence interval end
    %   - f : function reference
    %   - tolx : x axis max tolerance
    % Output:
    %   - x : root approximation
    %   - steps : required steps
    %
    imax = ceil(log2(b-a)-log2(tolx));
    for i=1:imax
        x = (a + b)/2;
        fa = feval(f, a);
        fb = feval(f, b);
        fx = feval(f, x);
        f1x = abs((fb-fa)/(b-a)); % derivative approximation
        if (abs(fx) <= tolx*f1x)
            break;
        elseif fa*fx < 0
            b = x;
        else % fa*fx > 0
            a = x;
        end         
    end
    steps = i;
end
