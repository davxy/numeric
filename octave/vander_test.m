% Plot the Vandermonde matrix condition number given an increasing
% matrix order

ordermax = 20;
vcond = zeros(ordermax,1);
axis = 1:ordermax;
for n = axis
    x = zeros(1,n);
    for i = 0:n
        x(i+1) = i/n;
    end
    A = vander(x);
    vcond(n) = cond(A);
end
semilogy(axis, vcond);
pause;
