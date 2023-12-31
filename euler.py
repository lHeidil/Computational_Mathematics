import numpy as np
from matplotlib import pyplot as plt
x_initial = 0
y_initial = 1
x_final = 10
sn = 101
delta_x = (x_final - x_initial) / (sn - 1)
x = np.linspace(x_initial, x_final, sn)
y = np.zeros([sn])
y [0] = y_initial
for i in range (1 , sn) :
    y [i] = delta_x * (-y[i - 1] + np.sin(x [i - 1])) + y [i - 1]
for i in range (sn) :
    print( x [i] , y [i] )
plt.plot ( x , y)
plt.xlabel(" Value of x ")
plt.ylabel("Value of y")
plt.title("Approximate S ol u ti o n with Forward Euler ’ s Method ")
plt.show ( )
