% TEST: Numeric Integration using adaptive Trapezoidal method

f = inline('-2*x^(-3) * cos(x^(-2))');
a = 0.5;
b = 100;
Iexp = sin(10^(-4)) - sin(4) % Expected integral value
set(gca, 'XScale', 'log');

%f = inline('0.2 + 25*x - 200*x^2 + 675*x^3 - 900*x^4 + 400*x^5');
%a = 0.0;
%b = 0.8;
%Iexp = 1.640533    % Expected integral value

tol = 10^(-2)       % Error tolerance

display('-------------------------------------------');
% Trapezoid adaptive method with relative error
[ I x ] = quad_trapezoid_adapt(a, b, f, tol);
E = abs(Iexp - I)/Iexp;   % relative error
n = length(x);
printf('> Trapezoid adaptive method\n I = %f\n E = %f\n n = %d\n', I, E, n);

% Trapezoid method with relative error
I = quad_trapezoid(a, b, f, n-1);
E = abs(Iexp - I)/Iexp;   % relative error
printf('> Trapezoid method\n I = %f\n E = %f\n n = %d\n', I, E, n);

% Simpson's method with relative error
I = quad_simpson(a, b, f, n-1);
E = abs(Iexp - I)/Iexp;
printf('> Simpson method\n I = %f\n E = %f\n n = %d\n', I, E, n);

display('-------------------------------------------');
% Simpson adaptive method with relative error
[ I x ] = quad_simpson_adapt(a, b, f, 10^(-4));
E = abs(Iexp - I)/Iexp;   % relative error
n = length(x);
printf('> Simpson adaptive method\n I = %f\n E = %f\n n = %d\n', I, E, n);

% Trapezoid method with relative error
I = quad_trapezoid(a, b, f, n-1);
E = abs(Iexp - I)/Iexp;   % relative error
printf('> Trapezoid method\n I = %f\n E = %f\n n = %d\n', I, E, n);

% Simpson's method with relative error
I = quad_simpson(a, b, f, n-1);
E = abs(Iexp - I)/Iexp;
printf('> Simpson method\n I = %f\n E = %f\n n = %d\n', I, E, n);


% Plot function graph using the last Simpson nodes
N = 10000;    % Number of points for a smooth plot
hold on
X = linspace(a, b, N);
Y = zeros(1, N);
for i = 1:N
    Y(i) = f(X(i));
end
plot(X, Y, 'b');
y = zeros(1,n);
for i = 1:n
    y(i) = f(x(i));
    %plot([x(i) x(i)], [0 y(i)], 'k');
end
plot(x, y, '+k')
hold off

% Wait for input
pause;
