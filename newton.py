# Importing Packages
import numpy as np
import matplotlib.pyplot as plt


# Defining Equation and Derivative
def f(x):
    res = np.cos(x) - 2 * x ** 3
    return res


def dfdx(x):
    res = -np.sin(x) - 6 * x ** 2
    return res

# Newton-Raphson Algorithm
max_iter = 20  # Max iterations
tol = 1E-15  # Tolerance
i = 0  # Iteration counter
x0 = 1  # Initial guess
xi_1 = x0
print('Iteration ' + str(i) + ': x = ' + str(x0) +  ', f(x) =' + str(f(x0)))
# Iterating until either the tolerance or max iterations is met
while abs(f(xi_1)) > tol or i > max_iter:
    i = i + 1
    xi = xi_1-f(xi_1)/dfdx(xi_1)  # Newton-Raphson equation
    print('Iteration'  + str(i) + ': x = ' + str(xi) +  ', f(x) ='  + str(f(xi)))
    xi_1 = xi

# Creating Data for the Line
x_plot = np.linspace(-2, 2, 1000)
y_plot = f(x_plot)

# Plotting Function
fig = plt.figure()
plt.plot(x_plot, y_plot, c='blue')
plt.plot(xi, f(xi), c='red', marker ='o', fillstyle ='none')
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()