# Explicit implementation of Runge-Kutta method of 4-th order to solving a differential equation of higher order ( 5th order ODE)
## This is a test case for a mathematical programmer position
The ODE example used in the test case is as follows
$$\frac{d^5y}{dx^5}+15\frac{d^4y}{dx^4}+90\frac{d^3y}{dx^3}+270\frac{d^2y}{dx^2}+405\frac{dy}{dx}+243y=0$$
with the initial conditions
$$\frac{d^4y}{dx^4}(0)=0; \ \frac{d^3y}{dx^3}(0)=-8;\ \frac{d^2y}{dx^2}(0)=-9; \ \frac{dy}{dx}(0)=0; \ y(0)=0$$
Because all initial conditions are set in the same point, namely 
$$x=0$$
We can solve the problem using Runge-Kutta method in its explicit formulation
The ODE is transformed into the following system of equations
$$\frac{dy}{dx}=d$$
$$\frac{d^2y}{dx^2}=c$$
$$\frac{d^3y}{dx^3}=b$$
$$\frac{d^4y}{dx^4}=a$$
$$\frac{d^5y}{dx^5}=-(15a+90b+270c+405d+243y)$$
Calculation interval is 
$$x\in[0,5]$$
