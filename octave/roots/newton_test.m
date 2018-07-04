% TEST: Newton method

format long

display('---------------------------------------------------------------------')
f  = inline('2^x-(cos(x+3))^2+exp(x+2)','x')
f1 = inline('(2^x)*log(2)-(2*cos(x+3)*-sin(x+3))+exp(x+2)','x')
display('> Newton plain')
[x,steps] = newton(0,f,f1,eps,100,1)
err = abs(feval(f,x))
display('> Newton chords')
[x,steps] = newton_chord(0,f,f1,eps,1000)
err = abs(feval(f,x))
display('> Newton secant')
[x,steps] = newton_secant(0,f,f1,eps,1000)
err = abs(feval(f,x))

display('---------------------------------------------------------------------')
f  = inline('log(sin(x+4)-cos(x-1))-exp(3*x-x^2)','x')
f1 = inline('(cos(x+4)+sin(x-1))/(sin(x+4)-cos(x-1))-exp(3*x-x^2)*(3-2*x)','x')
display('> Newton plain')
[x,steps] = newton(4,f,f1,eps,100,1)
err = abs(feval(f,x))

display('---------------------------------------------------------------------')
% 90 iterations are a too many for a method with quadratic convergence.
% Maybe the root has multiplicity > 1?
f  = inline('(4+log(x))*x*(log(x))^3','x')
f1 = inline('(log(x)^2)*((log(x)^2)+8*log(x)+12)','x')
display('> Netwon plain')
[x,steps] = newton(4,f,f1,eps,100,1)
err = abs(feval(f,x))
% With Aitken acceleration: 5 iterations
display('> With Aitken acceleration')
[x,steps] = newton_aitken(4,f,f1,eps,100)
err = abs(feval(f,x))
% The root multiplicity is 3, lets test the plain Newton method with
% known root multiplicity: 6 iterations
display('> Passing the root multiplicity to plain Newton (m=3)')
[x,steps] = newton(4,f,f1,eps,100,3)
err = abs(feval(f,x))
% Quasi-Newton method: chords
display('> Newton chords')
[x,steps] = newton_chord(4,f,f1,eps,5000)
err = abs(feval(f,x))
% Quasi-Newton method: secants
display('> Newton secants')
[x,steps] = newton_secant(4,f,f1,eps,5000)
err = abs(feval(f,x))

display('---------------------------------------------------------------------')
% The following function root computation with the plain Newton method is
% very inefficient. With 5000 steps the method converges with an error ~5E-7.
% Indeed the root has infinite multiplicity.
display('> Infinite multiplicity root')
f  = inline('sin(x-1)-0.5*sin(2*(x-1))','x')
f1 = inline('cos(x-1)-0.5*x*cos(2*(x-1))','x')
[x,steps] = newton(3,f,f1,eps,5000,1)
err = abs(feval(f,x))
% Same experiment but with Aitken acceleration
display('> With Aitken acceleration')
[x,steps] = newton_aitken(3,f,f1,eps,5000)
err = abs(feval(f,x))
% Quasi-Newton method: chords
display('> Newton chords')
[x,steps] = newton_chord(3,f,f1,eps,5000)
err = abs(feval(f,x))
% Quasi-Newton method: secants
display('> Newton secants')
[x,steps] = newton_secant(3,f,f1,eps,5000)
err = abs(feval(f,x))

display('---------------------------------------------------------------------')
% Even with a not so small error tolerance the plain Newton method takes too
% many steps to converge.
f  = inline('(3*x-9)^7','x')
f1 = inline('7*x*(3*x-9)^6','x')
display('> Plain Newton');
[x,steps] = newton(8,f,f1,1e-11,300,1)
err = abs(feval(f,x))
% The root multiplicity is clearly 7 => steps=8
display('> Known root multiplicity m=7')
[x,steps] = newton(8,f,f1,1e-11,300,7)
err = abs(feval(f,x))
% Quasi-Newton method: chords
display('> Newton chords')
[x,steps] = newton_chord(8,f,f1,1e-11,5000)
err = abs(feval(f,x))
% Quasi-Newton method: secants
display('> Newton secants')
[x,steps] = newton_secant(8,f,f1,1e-11,5000)
err = abs(feval(f,x))
