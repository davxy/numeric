% TEST: Bisection method

format long

tolx = eps

f  = inline('x^3-5*x','x')
f1 = inline('3*x^2-5','x')

display('> Try with Newton')
[x,steps] = newton(1,f,f1,eps,1000,1)
err = abs(feval(f,x))
if (err > tolx*abs(feval(f1,x)))
    display('> Non-convergence detected, fallback to Bisection')
    [x,steps] = bisect(-10,1,f,eps)
    err = abs(feval(f,x))
end
