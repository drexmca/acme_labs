# name this file 'solutions.py'
"""Volume II Lab 2: Object Oriented Programming
Donald Rex McArthur
Math 320
Sept. 10, 2015
"""

from Backpack import Backpack
import copy


# Problem 1: Modify the 'Backpack' class in 'Backpack.py'.
A = Backpack('red', 'Rex', 9)
# Study the 'Knapsack' class in 'Backpack.py'. You should be able to create a 
#   Knapsack object after finishing problem 1.


# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.
class Jetpack(Backpack):
    """A Jetpack object class. Inherits from the Backpack class.

    Attributes:
        color(str): color, defaults to silver
        name(str): name, defualts to jetback
        max_size(int): max number of elemetns, defaults to 2
        contents(list): Contents of jetback
        Fuel(int): Defaults to 10. Amount of fuel left in jetpack
    """
    def __init__(self, color='silver', name='jetpack', max_size=2, fuel = 10):
        """
        Constructor for jetpacks. Holds 2 items, has fuel attribute.

        Inputs:
            color(str): color, defaults to silver
            name(str): name, defualts to jetback
            max_size(int): max number of elemetns, defaults to 2
            contents(list): Contents of jetback
            Fuel(int): Defaults to 10. Amount of fuel left in jetpack

        Returns:
            an empty contented, 10 fuel filled silver jetpack
        """
        Backpack.__init__(self, color, name, max_size)
        self.fuel = 10

    def fly(self, burn):
        if burn < self.fuel:
            self.fuel -= burn
        else:
            print "Not enough Fuel!"

    def dump(self):
        self.fuel = 0
        self.contents = []
    pass

# Problem 3: write __str__ and __eq__ for the 'Backpack' class in 'Backpack.py'


# Problem 4: Write a ComplexNumber class.
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
        null = copy.copy(a)
        null.c = (-1*self.c)
        return null
    
    def norm(self):
        norm = ((self.r)**2 + (self.c)**2)**0.5
        return norm
    pass

# =============================== END OF FILE =============================== #
