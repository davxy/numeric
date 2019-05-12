% TEST: lagrange interpolation

% 3 points are sufficient to interpolate a polynomial of degree 2
x = [15 42 30];
y = x.^2;
% 100 evenly spaced values between 0 and 100
xx = linspace(0,100);
% interpolate to get yy values
yy = lagrange(xx,x,y);
% pre-computed y values are plotted with 'o',
% interpolated y values are plotted with '.'
plot(x,y,'o',xx,yy);
% Wait for input
pause;
