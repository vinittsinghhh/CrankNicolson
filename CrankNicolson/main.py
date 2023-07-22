import numpy as np
import matplotlib.pyplot as plt

# Geometry
L = 1.1  # in m

# x grid
x_step = 0.01  # in m
x_divisions = int(L/x_step) + 1
x = np.linspace(0, L, x_divisions)

# material properties
alpha = 1.2e-4   # in m^2/s

def CrankNicolson(t):
    for times in t:
        # time grid
        t_end = times  # in s
        t_step = 0.05  # in s
        nt = int(t_end/t_step)
        # initial value
        T_i = 300  # in K

        # define results parameter
        T = np.ones(x_divisions)*T_i

        # simulation
        for n in range(1, nt):
            Tn = T.copy()

            T[1:-1] = Tn[1:-1] + t_step * alpha * \
                (Tn[2:] - 2*Tn[1:-1] + Tn[0:-2])/(x_step)**2

            # defining boundary conditions
            T[0] = 350  # in K

            # gradient is zero at x=L so Last T value gets copied to last but one T value
            T[-1] = T[-2]

        #plotting the results
        plt.plot(x, T)

print("Enter end time: ", end = "")
endTime = int(input())
t = np.linspace(1, endTime, 20)
CrankNicolson(t)
plt.xlabel('x (in m)')
plt.ylabel('T(x) (in K)')
plt.show()