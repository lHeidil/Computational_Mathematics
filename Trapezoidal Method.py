from email.policy import default
import numpy as np
import matplotlib.pyplot as plt
import math

type_of_fn = int(input('Choose: \n1) Exp \n2) linear\n3) O.W. and you want to input your own funcion \n'))
#Defining The function to be integrated
if (type_of_fn == 3):
    fn = input("Enter you function (In terms of x): ")
def f(x):
    if type_of_fn==1:
        return pow(2.71,x)
    elif type_of_fn==2:
        return x
    elif type_of_fn==3:         
        return eval(fn)
    else:
        print ('WRONG!')



#Defining the Trapezoidal method
def trapezoidal(start,end,n):
    step_size = (end - start)/n
    sum = f(start) + f(end)

    for i in range(1,n):
        k = start + i*step_size
        sum = sum + 2*f(k)
    sum = sum * step_size/2
    
    
    return sum
lower_limit = float(input("Lower limit: "))
upper_limit = float(input("Upper limit: "))
sub_interval =int(input("Number of sub intervals: "))
ans=trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result = %f" %ans )