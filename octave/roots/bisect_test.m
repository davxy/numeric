% TEST: PA=LU Factorization

format long

f = inline('e^(x/10)-1','x')
[x,steps] = bisect(-2,1,f,eps)
err = abs(feval(f,x))

f = inline('sin(x)-(cos(x))^2','x')
[x,steps] = bisect(-1,1,f,eps)
err = abs(feval(f,x))

f = inline('x^2-8*x+2','x')
[x,steps] = bisect(0,5,f,eps)
err = abs(feval(f,x))

