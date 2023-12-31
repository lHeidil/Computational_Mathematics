from email.policy import default
from re import A
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

def bisection(start,end,iteration_number):
    if f(start)*f(end) >= 0:
        print("Bisection method fails.")
        return None
    a = start
    b = end
    for n in range(1,iteration_number+1):
        m = (a + b)/2
        f_m = f(m)
        if f(a)*f_m < 0:
            a = a
            b = m
        elif f(b)*f_m < 0:
            a = m
            b = b
        elif f_m == 0:
            print("Found exact solution.")
            return m
        else:
            print("Bisection method fails.")
            return None
    return (a + b)/2

start=float(input('Enter your start point: '))
end=float(input('Enter your end point: '))
iteration_number=int(input('Enter iteration number: '))

print('Result: ', bisection(start,end,iteration_number))
