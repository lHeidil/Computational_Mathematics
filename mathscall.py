from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap
from maths import Ui_MainWindow
import math

import numpy as np
import matplotlib.pyplot as plt
import sys

class MathsCall(QtWidgets.QMainWindow):
 
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        self.font.setBold(True)
        self.font.setWeight(175)
        self.ui.LinearRegressionButton.clicked.connect(self.LinearRegression)
        self.ui.ExponentialButton.clicked.connect(self.Exponential)
        self.ui.TrapezoidalButton.clicked.connect(self.Trapezoidal)
        self.ui.NewtonRaphsonButton.clicked.connect(self.NewtonRaphson)
        self.ui.SubIntervalNum.setMinimum(1)
        self.lst = ["exponential","linear"]
        self.ui.comboBox.addItems(self.lst)
        self.ui.comboBox.setEditable(True)

    def Exponential(self):
        x = np.arange(1, 21, 1)
        y = np.array([1, 3, 5, 7, 9, 12, 15, 19, 23, 28, 33, 38, 44, 50, 56, 64, 73, 84, 97, 113])
        f2 = plt.figure()
        ax2 = f2.add_subplot(111)
        ax2.scatter(x, y)
        imagePath = "Exp.png"
        plt.savefig(imagePath)
        pixmap = QPixmap(imagePath)
        resized = pixmap.scaled(int(pixmap.width()*7/10), int(pixmap.height()*7/10))
        self.ui.ExponentialLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.ExponentialLabel.setPixmap(QPixmap(resized))
        fit = np.polyfit(x, np.log(y), 1)
        # print(fit)
        y = math.e ** (fit[1] + (5 * fit[0]))
        # print(y)
        self.ui.ExponentialOut1Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.ExponentialOut2Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.ExponentialOut1Label.setFont(self.font)
        self.ui.ExponentialOut2Label.setFont(self.font)
        self.ui.ExponentialOut1Label.setText("ln(y) = " + str(fit[1]) + " + x * " + str(fit[0]))
        self.ui.ExponentialOut2Label.setText("y = " + str(y))

    def func(self,x):
        if self.type_of_fn=="exponential":
            return pow(2.71,x)
        elif self.type_of_fn=="linear":
            return x     
        else:
            return eval(self.type_of_fn)

    def trapezoidalcalculate(self,start,end,n,exp_values):
        step_size = (end - start)/n
        sum = self.func(start) + self.func(end)
        exp_values.append(float(self.func(start)))

        for i in range(1,n):
            k = start + i*step_size
            exp_values.append(float(2*self.func(k)))
            sum = sum + 2*self.func(k)
        sum = sum * step_size/2
        exp_values.append(float(self.func(end)))
        # print(exp_values)
        
        return sum

    def Trapezoidal(self):
        self.type_of_fn = self.ui.comboBox.currentText()
        lower_limit = float(self.ui.LowLimit.value())
        upper_limit = float(self.ui.UpLimit.value())
        sub_interval = int(self.ui.SubIntervalNum.value())
        exp_values=[]
        ans= self.trapezoidalcalculate(lower_limit, upper_limit, sub_interval,exp_values)
        self.ui.TrapezoidalOutLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.TrapezoidalOutLabel.setFont(self.font)
        self.ui.TrapezoidalOutLabel.setText("Integration = " + str(ans))
        tdata=np.linspace(lower_limit,upper_limit,100)
        tn=np.linspace(lower_limit,upper_limit, sub_interval+1)
        plt.figure()
        plt.subplot(211)
        plt.plot(tn,exp_values,'ro')
        plt.ylabel('Values of each interval')
        plt.subplot(212)
        plt.plot(tdata, self.func(tdata))
        plt.ylabel('f(x) function')
        plt.xlabel('x')
        # plt.show()
        imagePath = "Trapezoidal.png"
        plt.savefig(imagePath)
        pixmap = QPixmap(imagePath)
        resized = pixmap.scaled(int(pixmap.width()*7/10), int(pixmap.height()*7/10))
        self.ui.TrapezoidalLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.TrapezoidalLabel.setPixmap(QPixmap(resized))

    def f(self,x):
        res = np.cos(x) - 2 * x ** 3
        return res

    def f_prime(self,x):
        res = -np.sin(x) - 6 * x ** 2
        return res

    def NewtonRaphson(self):

        # Newton-Raphson Algorithm
        i_max = 20  # Max iterations
        tolerance = 1E-10  # Tolerance
        i = 0  # Iteration counter
        x0 = 1  # Initial guess
        xi1 = x0
        print('Iteration ' + str(i) + ': x = ' + str(x0) + ', f(x) =' + str(self.f(x0)))
        # Iterating until either the tolerance or max iterations is met
        while abs(self.f(xi1)) > tolerance or i > i_max:
            i = i + 1
            xi = xi1 - self.f(xi1) / self.f_prime(xi1)  # Newton-Raphson equation
            print('Iteration ' + str(i) + ': x = ' + str(xi) + ', f(x) =' + str(self.f(xi)))
            xi1 = xi
        # Creating Data for the Line
        x_plot = np.linspace(-2, 2, 1000)
        y_plot = self.f(x_plot)

        # Plotting Function
        fig = plt.figure()
        plt.plot(x_plot, y_plot, c='blue')

        # putting labels
        plt.xlabel('x')
        plt.ylabel('y')
        
        imagePath = "NewtonRaphson.png"
        plt.savefig(imagePath)
        pixmap = QPixmap(imagePath)
        resized = pixmap.scaled(int(pixmap.width()*7/10), int(pixmap.height()*7/10))
        self.ui.NewtonRaphsonLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.NewtonRaphsonLabel.setPixmap(QPixmap(resized))
        self.ui.NewtonRaphsonout1Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.NewtonRaphsonout1Label.setFont(self.font)
        self.ui.NewtonRaphsonout1Label.setText('Iteration ' + str(i) + ': x = ' + str(xi) + ', f(x) =' + str(self.f(xi)))

    def estimate_coef(self,x, y):
        # number of observations/points
        n = np.size(x)
     
        # mean of x and y vector
        m_x = np.mean(x)
        m_y = np.mean(y)
     
        # calculating cross-deviation and deviation about x
        SS_xy = np.sum(y*x) - n*m_y*m_x
        SS_xx = np.sum(x*x) - n*m_x*m_x
     
        # calculating regression coefficients
        b_1 = SS_xy / SS_xx
        b_0 = m_y - b_1*m_x
     
        return (b_0, b_1)
     
    def plot_regression_line(self,x, y, b):
        # plotting the actual points as scatter plot
        f1 = plt.figure()
        ax1 = f1.add_subplot(111)
        ax1.scatter(x, y, color = "m",
                   marker = "o", s = 30)
     
        # predicted response vector
        y_pred = b[0] + b[1]*x
     
        # plotting the regression line
        plt.plot(x, y_pred, color = "g")
     
        # putting labels
        plt.xlabel('x')
        plt.ylabel('y')
     
        # show plot in label
        imagePath = "LinearReg.png"
        plt.savefig(imagePath)
        pixmap = QPixmap(imagePath)
        resized = pixmap.scaled(int(pixmap.width()*7/10), int(pixmap.height()*7/10))
        self.ui.LinearRegressionLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.LinearRegressionLabel.setPixmap(QPixmap(resized))
     
    def LinearRegression(self):
        # observations / data
        x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
     
        # estimating coefficients
        b = self.estimate_coef(x, y)
        # print("Estimated coefficients:\nb_0 = {}  \
        #       \nb_1 = {}".format(b[0], b[1]))
        self.ui.LinearRegressionOut1Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.LinearRegressionOut2Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.LinearRegressionOut1Label.setFont(self.font)
        self.ui.LinearRegressionOut2Label.setFont(self.font)
        self.ui.LinearRegressionOut1Label.setText("b_0 = " + str(b[0]))
        self.ui.LinearRegressionOut2Label.setText("b_1 = " + str(b[1]))
     
        # plotting regression line
        self.plot_regression_line(x, y, b)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MathsCall()
    ui.show()
    sys.exit(app.exec_())