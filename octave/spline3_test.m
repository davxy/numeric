% Cubic spline interpolation test

nq = 100;   % query points
n  = 5; %15;    % number of interpolation nodes

% interpolation nodes
x = linspace(-1, 1, n);
y = 1 ./ (1 + 25*x.^2);

% Get function values over 100 evenly spaced values
X = linspace(min(x), max(x), nq);
f = 1 ./ (1 + 25*X.^2);

% Get yy values via interpolation
Y = spline3(x, y, X);

% pre-computed y values are plotted with 'o',
% interpolated y values are plotted with '.'
plot(X, Y, '+', X, f, x, y, 'o');

% Wait for input
pause;
