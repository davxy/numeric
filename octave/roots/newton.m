function [x,steps] = newton(x,f,f1,m,tolx,imax)
    %
    % Root finding Bisection method
    %
    % Input:
	%   - x  : first root approximation
	%   - f  : function reference
	%   - f1 : first derivative function reference
	%   - m  : root multiplicity;
	%           if 0 is unknown and Aitken acceleration is used.
	%   - tolx : max tolerance
	%   - imax : max iterations before stop trying
    % Output:
    %   - x     : final root approximation
    %   - steps : required steps
    %
    for i=1:imax
        fx = feval(f, x);
        f1x = feval(f1, x);
        if (abs(fx) <= tolx*f1x)
            break;
        end
        x = x - m*fx/f1x;
    end
    steps = i'