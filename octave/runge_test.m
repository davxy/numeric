% TEST: interpolation of Runge's function test

% Runge's function definition
rungef = inline('1.0/(1.0 + x^2)');

%
% Configuration
%
minpoints = 3;  % min number of nodes
maxpoints = 20; % max number of nodes
ibeg = -5;      % interval begin
iend =  5;      % interval end

function x = equis_nodes(a, b, n)
    x = linspace(a, b, n);
end

% Get equidistant nodes function handle
get_nodes = @equis_nodes;

xx = linspace(ibeg, iend, 100);
yy = arrayfun(rungef, xx);
for n = minpoints:3:maxpoints
    xpoints = get_nodes(ibeg, iend, n);
    ypoints = arrayfun(rungef, xpoints);
    yy1 = lagrange(xpoints, ypoints, xx);
    figure(n/3);
    plot(xx, yy, xx, yy1, xpoints, ypoints, 'o');
end

% Wait for input
pause;
