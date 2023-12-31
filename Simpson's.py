from email.policy import default
import numpy as np
import matplotlib.pyplot as plt
import math

from sympy import Sum

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

# Implementing Simpson's 1/3 
def simpson13(start,end,n):
    step_size = (end - start)/n
    sum = f(start) + f(end)
    
    for i in range(1,n):
        k = start + i*step_size

        if i%2 == 0:
            sum = sum + 2 * f(k)
        else:
            sum = sum + 4 * f(k)
    
    sum = sum * step_size/3
    
    return sum
    

lower_limit = float(input("Lower limit: "))
upper_limit = float(input("Upper limit: "))
sub_interval =int(input("Number of sub intervals: "))
ans = simpson13(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 1/3 method is: %f" %ans )