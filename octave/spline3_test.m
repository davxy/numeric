% Cubic spline interpolation test

nq = 100;   % query points
n  = 15;    % interpolation nodes

x = linspace(-1, 1, n);
y = zeros(1,n);
for i = 1:n
    y(i) = 1/(1 + 25*x(i)^2);
end

% 100 evenly spaced values between 0 and 100
X = linspace(min(x), max(x), nq);
% Get true function values
f = zeros(1,nq);
for i = 1:nq
    f(i)=1/(1 + 25*X(i)^2);
end
% Get yy values via interpolation
Y = spline3(x, y, X);

% pre-computed y values are plotted with 'o',
% interpolated y values are plotted with '.'
plot(X, Y, '+', X, f, x, y, 'o');

% Wait for input
pause;
