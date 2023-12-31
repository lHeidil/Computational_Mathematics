import math
def func(x,y):
    fn = (3*math.exp(-x))-(0.4*y) #Example of ordinary differential equation
    return fn

def heun():
    ##Initial Conditions
    x = 0 #Independent variable
    y = 5
    ##Integration Limit
    x_i=0
    x_f=3
    step_size=1.5 #stepsize

    print("Iteration",0)
    print("x:", x)
    print("y:",y)

    i=1
    n=(x_f-x_i)/step_size #number of iterations
    while i <= n:  #This loop will run until the number of iterations are completed
        k1 = func(x,y) #K1
        k2 = func(x+step_size,y+(k1*step_size)) #K2
        y = y+((k1+k2)*(step_size/2)) #Heun's formula to update y
        x = x+step_size #updating x
        print("Iteration",i)
        print("x:", x)
        print("y:",y)
        i = i + 1

def main():
    heun()

main()