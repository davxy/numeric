function y = lebesgue_const(xx, xpoints)
    y = 0;
    for i = 1 : length(xx)
        yy = lebesgue_func(xx(i), xpoints);
        if (yy > y)
            y = yy;
        end
    end
end

function sums = lebesgue_func(x, xpoints)
    n = length(xpoints);
    sums = 0.0;
    for i = 1:n
        L = 1.0;
        for j = 1:n
            if (i != j)
                L = L * (x - xpoints(j))/(xpoints(i)-xpoints(j));
            end
        end
        sums = sums + abs(L);
    end
end
