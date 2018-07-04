% TEST: Bisection method

format long

display('---------------------------------------------------------------------')
f = inline('sin(x)-(cos(x))^2','x')
[x,steps] = bisect(-1,1,f,eps)
err = abs(feval(f,x))

display('---------------------------------------------------------------------')
f = inline('x^2-8*x+2','x')
[x,steps] = bisect(0,5,f,eps)
err = abs(feval(f,x))

display('---------------------------------------------------------------------')
f = inline('2^x-(cos(x+3))^2+exp(x+2)','x')
[x,steps] = bisect(-10,10,f,eps)
err = abs(feval(f,x))

