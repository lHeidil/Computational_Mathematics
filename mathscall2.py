from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap
from output import Ui_MainWindow
import math
from sympy import N
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
        self.ui.powerButton.clicked.connect(self.Power)
        
    def Exponential(self):
        x = np.arange(1, 21, 1)
        y = np.array([1, 3, 5, 7, 9, 12, 15, 19, 23, 28, 33, 38, 44, 50, 56, 64, 73, 84, 97, 113])
        f2 = plt.figure()
        ax2 = f2.add_subplot(111)
        ax2.scatter(x, y)
        fit = np.polyfit(x, np.log(y), 1)
        # print(fit)
        y = math.e ** (fit[1] + (5 * fit[0]))
        x2 = np.linspace(0, 21, 20)
        y2 = math.e ** (fit[1] + (x * fit[0]))
        plt.plot(x2, y2)
        imagePath = "Exp.png"
        plt.savefig(imagePath)
        pixmap = QPixmap(imagePath)
        self.ui.ExponentialLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.ExponentialLabel.setPixmap(QPixmap(pixmap))
        # print(y)
        self.ui.ExponentialOut1Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.ExponentialOut2Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.ExponentialOut1Label.setFont(self.font)
        self.ui.ExponentialOut2Label.setFont(self.font)
        self.ui.ExponentialOut1Label.setText("ln(y) = " + str(fit[1]) + " + x * " + str(fit[0]))
        self.ui.ExponentialOut2Label.setText("y = " + str(y))

    def Power(self):
        x = np.array([6, 7, 7, 8, 12, 14, 15, 16, 16, 19])
        y = np.array([14, 15, 15, 17, 18, 18, 19, 24, 25, 29])
        f3 = plt.figure()
        ax3 = f3.add_subplot(111)
        ax3.scatter(x, y)
        fit = np.polyfit(np.log(x), np.log(y), 1)
        #print(fit)
        y = (math.e ** fit[1]) * (5 ** fit[0])
        x3 = np.linspace(0, 19, 20)
        y3 = (math.e ** fit[1]) * (x3 ** fit[0])
        plt.plot(x3, y3)
        imagePath = "Power.png"
        plt.savefig(imagePath)
        pixmap = QPixmap(imagePath)
        self.ui.powerLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.powerLabel.setPixmap(QPixmap(pixmap))    
        #print(y)
        self.ui.powerOutLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.powerOut2Label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.powerOutLabel.setFont(self.font)
        self.ui.powerOut2Label.setFont(self.font)
        self.ui.powerOutLabel.setText("y = " + str((math.e ** fit[1])) + " * x ^ " + str(fit[0]))
        self.ui.powerOut2Label.setText("y = " + str(y))

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
        self.ui.LinearRegressionLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.LinearRegressionLabel.setPixmap(QPixmap(pixmap))
     
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