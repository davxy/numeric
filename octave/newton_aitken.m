function [x,steps] = newton_aitken(x,f,f1,tolx,imax)
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
    for i=1:imax
        % The first point is computed using plain Newton
        fx  = f(x);
        f1x = f1(x);
        if (abs(fx) <= tolx*abs(f1x))
            break;
        end
        x1 = x-fx/f1x;
        % The second point is computed using plain Newton
        fx  = f(x1);
        f1x = f1(x1);
        if (abs(fx) <= tolx*abs(f1x))
            x = x1;
            break;
        end
        x2 = x1-fx/f1x;
        # Aitken acceleration
        x = (x1*x1-x*x2)/(2*x1-x2-x);
    end
    steps = i;
end
