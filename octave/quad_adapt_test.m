% TEST: Numeric Integration using adaptive Trapezoidal method

f = inline('-2*x^(-3) * cos(x^(-2))');
a = 0.5;
b = 100;
Iexp = sin(10^(-4)) - sin(4) % Expected integral value

#f = inline('0.2 + 25*x - 200*x^2 + 675*x^3 - 900*x^4 + 400*x^5');
#a = 0.0;
#b = 0.8;
#Iexp = 1.640533    % Expected integral value

N = 10000;    % Number of points for the smooth plot

%------------------------------------------------------------------------------

% Trapezoid adaptive method with relative error
display('> Trapezoid adaptive method');
[ I x ] = quad_trapezoid_adapt(a, b, f, 10^(-4));
n = length(x)
I
E = abs(Iexp - I)/Iexp   % relative error

% Trapezoid method with relative error
display('> Trapezoid method');
I = quad_trapezoid(a, b, f, n)
E = abs(Iexp - I)/Iexp   % relative error

% 1/3 Simpson's method with relative error
display('> Simpson method');
I = quad_simpson(a, b, f, n)
E = abs(Iexp - I)/Iexp

%------------------------------------------------------------------------------

% Simpson adaptive method with relative error
display('> Simpson adaptive method');
[ I x ] = quad_simpson_adapt(a, b, f, 10^(-4));
n = length(x)
I
E = abs(Iexp - I)/Iexp   % relative error

% Trapezoid method with relative error
display('> Trapezoid method');
I = quad_trapezoid(a, b, f, n)
E = abs(Iexp - I)/Iexp   % relative error

% 1/3 Simpson's method with relative error
display('> Simpson method');
I = quad_simpson(a, b, f, n)
E = abs(Iexp - I)/Iexp


#set(gca, 'XScale', 'log');
hold on
X = linspace(a, b, N);
Y = zeros(1, N);
for i = 1:N
    Y(i) = f(X(i));
endfor
plot(X, Y, 'b');
y = zeros(1,n);
for i = 1:n
    y(i) = f(x(i));
#    plot([x(i) x(i)], [0 y(i)], 'k');
endfor
plot(x, y, '+k')
hold off

% Wait for input
%pause;
