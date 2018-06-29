% TEST: cubic spline interpolation

nq = 100;   % query points
n  = 50;     % interpolation nodes

x = linspace(-1,1,n);
for i=1:n
    y(i)=1/(1 + 25*x(i)^2);
end

% 100 evenly spaced values between 0 and 100
xx = linspace(min(x),max(x),100);

% Get true function values
for i=1:nq
    ff(i)=1/(1 + 25*xx(i)^2);
end

% interpolate to get yy values
yy = spline(x,y,xx);

%yy = lagrange(xx,x,y);
% pre-computed y values are plotted with 'o',
% interpolated y values are plotted with '.'
plot(xx,yy,'+',xx,ff,x,y,'o');
