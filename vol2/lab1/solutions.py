# name this file 'solutions.py'
"""Volume II Lab 1: The Standard Library
Donald Rex McArthur
Sept. 2, 2015
Math 321
"""

# Add import statements here.
import sys
import time
import numpy as np
import matrix_multiply 
import example_module
import calculator as calc
# In future labs, do not modify any PROVIDED import statements.
# You may always add others as needed.


# Problem 1: Implement this function.
def prob1(l):
    """Accept a list 'l' of numbers as input and return a new list with the
    minimum, maximum, and average of the contents of 'l'.
    """
    data = np.zeros(3)
    data[0] = min(l)
    data[1] = max(l)
    data[2] = float(sum(l))/len(l)
    return data 
#print prob1([4,5,4,3,2,32])


# Problem 2: Implement this function.
def prob2():
    """Determine which Python objects are mutable and which are immutable. Test
    numbers, strings, lists, tuples, and dictionaries. Print your results to the
    terminal using the print() function.
    """
    print 'Numbers, strings, tuples are immutable, lists, dictionaries are mutable'
    pass

# Problem 3: Create a 'calculator' module and use it to implement this function.
def prob3(a,b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any methods other than those that are imported from the
    'calculator' module.
    
    Parameters:
        a (float): the length one of the sides of the triangle.
        b (float): the length the other nonhypotenuse side of the triangle.
    
    Returns:
        The length of the triangle's hypotenuse.
    """
    leg = calc.root(calc.add(calc.square(a),calc.square(b)))
    return leg
#print prob3(3,4)

# Problem 4: Utilize the 'matrix_multiply' module and 'matrices.npz' file to
#   implement this function.
def prob4():
    """If no command line argument is given, print "No Input."
    If anything other than "matrices.npz is given, print "Incorrect Input."
    If "matrices.npz" is given as a command line argument, use functions
    from the provided 'matrix_multiply' module to load two matrices, then
    time how long each method takes to multiply the two matrices together.
    Print your results to the terminal.
    """
    if len(sys.argv) < 2:
        print 'No Input.'
    else:
        if sys.argv[1] != 'matrices.npz':
            print 'Incorrect Input.'
        else:
            a,b = matrix_multiply.load_matrices(sys.argv[1])
            start = time.time()
            matrix_multiply.method1(a,b)
            print 'Method 1 took {} sec.'.format(time.time()-start)
            start = time.time()
            matrix_multiply.method2(a,b)
            print 'Method 2 took {} sec.'.format(time.time()-start)
            start = time.time()
            matrix_multiply.method3(a,b)
            print 'Method 3 took {} sec.'.format(time.time()-start)
            
            
    
    pass


# Everything under this 'if' statement is executed when this file is run from
#   the terminal. In this case, if we enter 'python solutions.py word' into
#   the terminal, then sys.argv is ['solutions.py', 'word'], and prob4() is
#   executed. Note that the arguments are parsed as strings. Do not modify.
if __name__ == "__main__":
    prob4()


# ============================== END OF FILE ================================ #
