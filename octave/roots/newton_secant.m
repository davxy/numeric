function [x,steps] = newton_secant(x,f,f1,tolx,imax)
    %
    % Newton root finding method  with Aitken acceleration
    %
    % Input:
    %   - x  : first root approximation
    %   - f  : function reference
    %   - f1 : first derivative function reference
    %   - tolx : max tolerance
    %   - imax : max iterations before stop trying
    % Output:
    %   - x     : final root approximation
    %   - steps : required steps
    %
    % Compute a second point using the plain Newton method
    fx0  = f(x);
    f1x0 = f1(x);
    x0   = x;
    x    = x0 - fx0/f1x0;
    for i=1:imax
        fx  = f(x);
        f1x = f1(x);
        if (abs(fx) <= tolx*f1x || fx == fx0)
            break;
        end
        tmp = x;
        x = x - fx*(x-x0)/(fx-fx0);
        x0 = tmp;
        fx0 = fx;
    end
    steps = i;
    return
