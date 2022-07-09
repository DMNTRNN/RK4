import numpy as np
import matplotlib.pyplot as plt



# We represent the ODE as the following system of equtaions. Each function corresponds an equation of the system
#in the following way f1=da/dx f2=db/dx=a; f3=dc/dx=b; f4=dd/dx=c;* f5=dy/dx=d
# Generally, each of the functions above is f(x, a, b, c, d, y). And thus, the ODE of 5th order can be represented as the system of 5 equations
#*-Sorry for notation abuse on this one

def f5(x, a, b, c, d, y):
    return d


def f4(x, a, b, c, d, y):
    return c


def f3(x, a, b, c, d, y):
    return b


def f2(x, a, b, c, d, y):
    return a


def f1(x, a, b, c, d, y):
    return -(15 * a + 90 * b + 270 * c + 405 * d + 243 * y)


# For convenience, we wrap all those functions into a function of a tuple argument, that returns an array 
def fn_list(tup):
    x = tup[0]
    a = tup[1]
    b = tup[2]
    c = tup[3]
    d = tup[4]
    y = tup[5]
    return np.array(
        (
            x,
            f1(x, a, b, c, d, y),
            f2(x, a, b, c, d, y),
            f3(x, a, b, c, d, y),
            f4(x, a, b, c, d, y),
            f5(x, a, b, c, d, y),
        )
    )  


# Now, RK4 itself
def RK4(h, x_0, y4_0, y3_0, y2_0, y1_0, y_0):# x_0 is an initial coordinate from which the calculation starts, then the initial conditions follow
    args = (x_0, y4_0, y3_0, y2_0, y1_0, y_0)
    k1 = h * fn_list(
        (x_0, y4_0, y3_0, y2_0, y1_0, y_0)
    )  # array of k1 koefficients ( each equation of the system has its separate k1,k2,k3,k4 koefficients)
    k2args = tuple(
        i[0] + i[1] / 2 for i in zip(args, k1)
    )  # array of args for calculating k2
    k2 = h * fn_list(k2args)  # array of k2
    k3args = tuple(
        i[0] + i[1] / 2 for i in zip(args, k2)
    )  # args for k3
    k3 = h * fn_list(k3args)  #  array of k3
    k4args = tuple(
        i[0] + i[1] for i in zip(args, k3)
    )  #  args for k4
    k4 = h * fn_list(k4args)  # array of k4
    new_vals = list(
        args
    )  # values of functions in the next step x=x_0+h
    new_vals[0] = new_vals[0] + h  # update the x value
    for i in range(1, 6):
        new_vals[i] = new_vals[i] + (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6  # update function values at the point x=x_0+h
    return new_vals


# The above procedure allows to calculate one step forward. The following procedure allow to repeat the procedure N times to achieve upper limit x=verh
def PROCEDURE(verh, h, x_0, y4_0, y3_0, y2_0, y1_0, y_0):
    steps = (
        int((verh - x_0) / h) + 1
    )  # calculating number of steps required to achieve x=verh
    rez = np.zeros((steps, 2))  # results are written inti this array
    for i in range(steps):
        (x_0, y4_0, y3_0, y2_0, y1_0, y_0) = RK4(h, x_0, y4_0, y3_0, y2_0, y1_0, y_0)
        rez[i, 0] = x_0
        rez[i, -1] = y_0
    return rez


# Initial conditions according to the example
x_0 = 0
y_0 = 0
y1_0 = 3
y2_0 = -9
y3_0 = -8
y4_0 = 0

# Upper limit of calcilation
verh = 5

# Let's plot few lines with different h to check stability of the method
h = 0.25
m = PROCEDURE(verh, h, x_0, y4_0, y3_0, y2_0, y1_0, y_0)
t = m[:, 0]
s = m[:, 1]

h = 0.001
m = PROCEDURE(verh, h, x_0, y4_0, y3_0, y2_0, y1_0, y_0)
t1 = m[:, 0]
s1 = m[:, 1]


fig, ax = plt.subplots()
ax.plot(t, s)
ax.plot(t1, s1)


# From the graph we see, that calculating scheme is stable


ax.set(xlabel="х", ylabel="у", title="Stability check")
ax.grid()

fig.savefig("Graph.png")
plt.show()

