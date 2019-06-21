% TEST: Numeric Integration using Trapezoidal and 1/3 Simpson methods

f = inline('0.2 + 25*x - 200*x^2 + 675*x^3 - 900*x^4 + 400*x^5');

a = 0.0;
b = 0.8;
N = 100;    % Number of points for the smooth plot
n = 10;      % Integration points (segments = n-1)

Iexp = 1.640533    % Expected integral value

hold on
X = linspace(a, b, N);
Y = zeros(1, N);
for i = 1:N
    Y(i) = f(X(i));
endfor
plot(X, Y, 'b');
X = linspace(a, b, n);
Y = zeros(1,n);
for i = 1:n
    Y(i) = f(X(i));
    plot([X(i) X(i)], [0 Y(i)], '--k');
endfor
plot(X, Y, '--k')
hold off

% Trapezoid rule with relative error
I = quad_trapezoid(a, b, f, n-1)
E = abs(Iexp - I)/Iexp   % relative error

% 1/3 Simpson's rule with relative error
I = quad_simpson(a, b, f, n-1)
E = abs(Iexp - I)/Iexp

% Wait for input
pause;
