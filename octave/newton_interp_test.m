% TEST: newton interpolation

% 3 points are sufficient to interpolate a polynomial of degree 2
x = [15 42 35];
y = sin(x);

% 100 evenly spaced values between 0 and 100
X = linspace(10, 50, 100);
% interpolate to get yy values
Y = newton_interp(x, y, X);

% pre-computed y values are plotted with 'o',
% interpolated y values are plotted with '.'
plot(x, y, 'o', X, Y);
% Wait for input
pause;

% Add a new node
x = [ x, 20 ]
y = [ y, sin(20) ]
L = ones(1, size(X, 2));
n = size(x, 2);
for i = 1:(n-1)
    L = L .* (X - x(i));
end   
a = divdiff(x, y);
Y = Y + a*L;

% pre-computed y values are plotted with 'o',
% interpolated y values are plotted with '.'
plot(x, y, 'o', X, Y);
% Wait for input
pause;
