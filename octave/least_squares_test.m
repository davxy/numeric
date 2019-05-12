% Interpolation interval
xmin = -pi
xmax =  pi
% Function
f = @(x) sin(x)
%f = @(x) 4*x
% Number of samples
s = 30
% Interpolating polynomial degree
d = 3

% Sample points
x = linspace(xmin, xmax, s)';
y = f(x) + (-1 + 2*rand(s,1));
% Query points
X = linspace(xmin, xmax, 100);
% Evaluation
Y = least_squares(x, y, d, X);

% Plot results
L=length(X)
plot(x, y, 'o', X, Y);
pause;
