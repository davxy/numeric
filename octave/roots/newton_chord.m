function [x,steps] = newton_chord(x,f,f1,tolx,imax)
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
    f1x = feval(f1, x);
    for i=1:imax
        fx = feval(f, x);
        if (abs(fx) <= tolx*f1x)
            break;
        end
        x = x - (fx/f1x);
    end
    steps = i;
    return