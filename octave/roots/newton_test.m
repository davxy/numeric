% TEST: Newton method

format long

f  = inline('2^x-(cos(x+3))^2+exp(x+2)','x')
f1 = inline('(2^x)*log(2)-(2*cos(x+3)*-sin(x+3))+exp(x+2)','x')
[x,steps] = newton(0,f,f1,1,eps,100)
err = abs(feval(f,x))

