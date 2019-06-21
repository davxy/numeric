% TEST: Numeric Integration using Trapezoidal and Simpson methods

f = inline('0.2 + 25*x - 200*x^2 + 675*x^3 - 900*x^4 + 400*x^5');
a = 0.0;
b = 0.8;
Iexp = 1.640533  % Expected integral value

%f = inline('sin(x)');
%a = 0.0;
%b = pi;
%Iexp = -cos(b) + cos(a)  % Expected integral value

% n: the number of integration nodes (segments = n-1)
for n = 2:2:10
    display('-----------------------------------');
    printf('n = %d\n', n);

    % Trapezoid method with relative error
    I = quad_trapezoid(a, b, f, n-1);
    E = abs(Iexp - I)/Iexp;
    printf('> Trapezoid : I = %f, E = %f\n', I, E);

    % Simpson's method with relative error
    I = quad_simpson(a, b, f, n-1);
    E = abs(Iexp - I)/Iexp;
    printf('> Simpson   : I = %f, E = %f\n', I, E);
end

% Plot using the last approximation number of nodes
N = 1000;    % Number of points for smooth function plot
hold on
X = linspace(a, b, N);
Y = zeros(1, N);
for i = 1:N
    Y(i) = f(X(i));
end
plot(X, Y, 'b');
X = linspace(a, b, n);
Y = zeros(1,n);
for i = 1:n
    Y(i) = f(X(i));
    plot([X(i) X(i)], [0 Y(i)], '--k');
end
plot(X, Y, '--k')
hold off

% Wait for input
pause;
