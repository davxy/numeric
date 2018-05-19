function y=lagrange(x,xpoints,ypoints)
    %
    % Lagrange interpolation method.
    %
    % Input:
    %   - x : points to evaluate x axis
    %   - xpoints: precomputed points x axis values
    %   - ypoints: precomputed points y axis values
    % Output:
    %   - y : interpolated points y axis
    %
    % Assumes that all the input values are row vectors.
    %
    if (size(xpoints,2) != size(ypoints,2))
        error('xpoints and ypoints must have the same number of elements')
    end
    n = size(xpoints,2);
    L = ones(n,size(x,2));
    for i=1:n
        for j=1:n
            if (i!=j)
                L(i,:)=L(i,:).*(x-xpoints(j))/(xpoints(i)-xpoints(j));
            end
        end
   end
   y=zeros(n,size(x,2));
   for i=1:n
      y=y+ypoints(i)*L(i,:);
   end
