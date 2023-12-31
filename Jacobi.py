from email.policy import default
import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import N

fn1 = input('please write 1st eqn in terms of X: ')
fn2 = input('please write 2nd eqn in terms of Y: ')
fn3 = input('please write 3rd eqn in terms of Z: ')

fn_1 = lambda x,y,z: eval(fn1)
fn_2 = lambda x,y,z: eval(fn2)
fn_3 = lambda x,y,z: eval(fn3)

x0=float(input('Enter initial value of X: '))
y0=float(input('Enter initial value of y: '))
z0=float(input('Enter initial value of z: '))

number_of_rep=int(input('enter number of itirations: '))

for i in range(1,number_of_rep):
    x1 = fn_1(x0,y0,z0)
    y1 = fn_2(x0,y0,z0)
    z1 = fn_3(x0,y0,z0)
    print('%d\t%f\t%f\t%f\n' %(i, x1,y1,z1))
    x0=x1
    y0=y1
    z0=z1
    