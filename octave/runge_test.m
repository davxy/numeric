% TEST: interpolation of Runge's function test

% Runge's function definition
rungef = inline('1.0/(1.0 + x^2)');

%
% Configuration
%
minpoints = 3;  % min number of nodes
maxpoints = 20; % max number of nodes
step = 2;       % step between nodes
ibeg = -5;      % interval begin
iend =  5;      % interval end

% Returns a list of equidistant nodes over [a,b]
function x = equis_nodes(a, b, n)
    x = linspace(a, b, n);
end

% Returns a list of n Chebyshev nodes over [a,b]
function x = cheby_nodes(a, b, n)
    for i = 1:n
        % Chebyscev nodes over the interval [-1,1]
        x(i) = cos((2*(i-1)+1)*pi/(2*n));
        % Affine transformation to the interval [a,b]
        x(i) = (a+b)/2 + (b-a)/2 * x(i);
    end
end

% Get equidistant nodes function handle
%get_nodes = @equis_nodes;
get_nodes = @cheby_nodes;

xx = linspace(ibeg, iend, 100);
yy = arrayfun(rungef, xx);
for n = minpoints:step:maxpoints
    % Graph plot
    xpoints = get_nodes(ibeg, iend, n);
    ypoints = arrayfun(rungef, xpoints);
    yy1 = lagrange(xpoints, ypoints, xx);
    figure(n);
    plot(xx, yy, xx, yy1, xpoints, ypoints, 'o');
    % Print Lebesgue constant on the console
    lamb = lebesgue_const(xx, xpoints);
    printf('n=%d, labda=%f\n', n, lamb);
end

% Wait for input
pause;
