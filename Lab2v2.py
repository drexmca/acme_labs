import numpy as np
from PySide import QtGui, QtCore
import sys
from cmath import sqrt

##Problem 1

class people(object):
    def __init__(self, type = ""):
        self.type = type
        self.classes = []
    
    def add_class(self, class1):
        self.classes.append(class1)

    def remove_class(self, class1):
        return self.classes.pop(self.classes.index(class1))


Rick = people(type="Professor")
Rick.add_class("Econ")
Rick.remove_class("Econ")

#Problem 2
class ComplexNumber(object):
    """
    This is a class the keeps and operates on complex number objects
    ### Methods ###
    __init__: sets the real value and complex value to 0 by default
    __repr__: creates a printable object 
    __sub__: subtracts using complex subtraction
    __add__: adds using complex addition
    __mult__: multiplies using complex multiplication
    __div__: divides using complex division
    norm: Checks the distance between the two complex objects
    __lt__: checks if it is less than, using distance from origin
    __gt__: Checks if it is greater than, using distance from orgin
    __eq__: Checks for equality, using distance from origin
    """
    def __init__ (self, r = 0., c = 0.):
        self.r = float(r)
        self.c = float(c)
    
    def __repr__(self):
        if self.r != 0.0 and self.c > 0.0:
            return str(self.r) + "+" + str(self.c) + "j"
        if self.r != 0.0 and self.c < 0.0:
            return str(self.r) +  str(self.c) + "j"
        if self.r == 0.0 and self.c != 0.0:
            return str(self.c) + "j"
        if self.r != 0.0 and self.c == 0.0:
            return str(self.r)
    
    def __sub__(self, other):
        a = self.r
        b = self.c
        c = other.r
        d = other.c
        
        null = ComplexNumber()
        null.r = a-b
        null.c = b-d
        
        return null

    def __add__(self, other):
        a = self.r
        b = self.c
        c = other.r
        d = other.c
        
        null = ComplexNumber()
        null.c = b + d
        null.r = a + c
        return null
    
    def __mul__(self, other):
        a = self.r
        b = self.c
        c = other.r
        d = other.c
        
        null = ComplexNumber()
        null.r = (a*c - b*d)
        null.c = (a*d + b*c)
        return null
    
    def __div__(self, other):
        a = self.r
        b = self.c
        c = other.r
        d = other.c
        
        null = ComplexNumber()
        null.r = (a*c + b*d)/((c**2)+(d**2))
        null.c = (b*c - a*d)/((c**2)+(d**2))
        return null
    
    def __eq__(self, other):
        a = self.r
        b = self.c
        c = other.r
        d = other.c
        
        self_norm = np.sqrt(a**2 + b**2)
        other_norm = np.sqrt(c**2 + d**2)
        
        return self_norm == other_norm
        
    def __lt__(self, other):
        a = self.r
        b = self.c
        c = other.r
        d = other.c
        
        self_norm = np.sqrt(a**2 + b**2)
        other_norm = np.sqrt(c**2 + d**2)
        
        return self_norm < other_norm
    
    def __gt__(self, other):
        a = self.r
        b = self.c
        c = other.r
        d = other.c
        
        self_norm = np.sqrt(a**2 + b**2)
        other_norm = np.sqrt(c**2 + d**2)
        
        return self_norm > other_norm
    
    def conjugate(self):
        null = self
        null.c = (-1*self.c)
        return null
    
    def norm(self, other):
        null = ComplexNumber()
        
        norm = ((self.r-other.r)**2 + (self.c - other.c)**2)**0.5
        return norm

a = ComplexNumber(2,2)
b = ComplexNumber(6,6)

a+b
(b-a)
a*b
a/b
a == b
a > b
a < b
a.conjugate()
a.norm(b)

## Problem 3

class Quad(QtGui.QWidget):
    def __init__(self):
        super(Quad, self).__init__()
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.p_root = 0.0
        self.n_root = 0.0
        self._init_boxes()
    def _init_boxes(self):
        self.label_positive_root = QtGui.QLabel()
        self.label_positive_root.setText("Positive Root:" + "\t\t\t" + str(self.p_root))
        self.label_negative_root = QtGui.QLabel()
        self.label_negative_root.setText("Negative Root:" + "\t\t\t" + str(self.n_root))

        aBar = QtGui.QDoubleSpinBox()
        bBar = QtGui.QDoubleSpinBox()
        cBar = QtGui.QDoubleSpinBox()

        aBar.setRange(-1000, 1000)
        bBar.setRange(-1000, 1000)
        cBar.setRange(-1000, 1000)

        aBar.setDecimals(5)
        bBar.setDecimals(5)
        cBar.setDecimals(5)

        aBar.valueChanged.connect(self.update_a)
        bBar.valueChanged.connect(self.update_b)
        cBar.valueChanged.connect(self.update_c)
        aBar.valueChanged.connect(self.updateRoots)
        bBar.valueChanged.connect(self.updateRoots)
        cBar.valueChanged.connect(self.updateRoots)
        
        vbox = QtGui.QVBoxLayout()

        vbox.addWidget(aBar, 0, 0)
        vbox.addWidget(bBar, 1, 0)
        vbox.addWidget(cBar, 2, 0)
        vbox.addWidget(self.label_positive_root, 3, 0)
        vbox.addWidget(self.label_negative_root, 4, 0)

        self.setLayout(vbox)

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle("Quadratic Roots")
        self.show()

    def updateRoots(self):
        self.label_positive_root.setText("Positive Root:" + "\t\t\t" + str(self.p_root))
        self.label_negative_root.setText("Negative Root:" + "\t\t\t" + str(self.n_root))

    def update_a(self, a):
        self.a = a
        self.root()

    def update_b(self, b):
        self.b = b
        self.root()

    def update_c(self, c):
        self.c = c
        self.root()

    def root(self):
        try:

            self.p_root = ((-self.b + sqrt(self.b**2 -
                4*self.a*self.c))/(2*self.a))

            self.n_root = ((-self.b - sqrt(self.b**2 -
                4*self.a*self.c))/(2*self.a))
        except ZeroDivisionError:
            a=1


            
def main():

    app = QtGui.QApplication(sys.argv)

    q = Quad()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

