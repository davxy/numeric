gamma = 0.1
x = linspace(0, 10, 101)';
y = 10*x+5+(sin(x*pi))*gamma;

plot(x, y);

pause;
