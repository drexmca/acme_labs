#solutions.py
"""Volume I Lab 1: Getting Started
Donald Rex McArthur
Math 321
Sept. 2, 2015
"""
import string
import numpy as np


# Problem 1: Write and run a "Hello World" script.
print('Hello World')

# Problem 2: Implement this function.
def sphere_volume(r):
    """Return the volume of the sphere of radius 'r'."""
    pi = 3.14159
    return  (4./3)*pi*r**3


# Problem 3: Implement the first_half() and reverse() functions.
def first_half(my_string):
    """Return the first half of the string 'my_string'.

    Example:
        >>> first_half("python")
        'pyt'
    """
    length = len(my_string)
    a =  my_string[:length/2]
    return a
first_half('Python')

def reverse(my_string):
    """Return the reverse of the string 'my_string'.
    
    Example:
        >>> reverse("python")
        'nohtyp'
    """
    a = my_string[::-1]
    return a

reverse('HELLLLLO')
    
# Problem 4: Perform list operations
# For the grader, do not change the name of 'my_list'.
my_list =  ["ant", "baboon", "cat", "dog"] 

# Put your code here
my_list.append('elephant')
my_list.remove('ant')
my_list.remove(my_list[1])
my_list[2] = 'donkey'
my_list.append('fox')
print my_list

    
# Problem 5: Implement this function.
def pig_latin(word):
    """Translate the string 'word' into Pig Latin
    
    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    if word[0]=='a' or 'e' or 'i' or 'o'  or 'u' or 'y':
        pig = str(word[1:]) + 'hay'
    else:
        pig = str(word[1:])+str(word[0])+'ay'   
    return pig 
        
print pig_latin('university')
# Problem 6: Implement this function.
def int_to_string(my_list):
    """Use a dictionary to translate a list of numbers 1-26 to corresponding
    lowercase letters of the alphabet. 1 -> a, 2 -> b, 3 -> c, and so on.
    
    Example:
        >>> int_to_string([13, 1, 20, 8])
        ['m', 'a', 't', 'h'] 
    """
    letters = list(string.ascii_lowercase)
    numbers = range(1,27)
    translate = dict(zip(numbers, letters))
    word = []
    for number in my_list:
        word.append(translate[number])
    return word
print int_to_string([13,1,20,8])


# Problem 7: Implement this generator.
def squares(n):
    """Yield all squares less than 'n'.

    Example:
        >>> for i in squares(10):
        ...     print(i)
        ... 
        0
        1
        4
        9
    """
    i = 0
    while i**2 < n:
        yield i**2
        i += 1
    pass

x = squares(10)
print next(x)
print next(x)
print next(x)

# Problem 8: Implement this function.
def stringify(my_list):
    """Using a list comprehension, convert the list of integers 'my_list'
    to a list of strings. Return the new list.

    Example:
        >>> stringify([1, 2, 3])
        ['1', '2', '3']
    """
    return [str(n) for n in my_list]

# Problem 9: Implement this function and use it to approximate ln(2).
def alt_harmonic(n):
    """Return the partial sum of the first n terms of the alternating
    harmonic series. Use this function to approximae ln(2).
    """
    x = xrange(1, n+1)
    x = np.array([float(i) for i in x])
    x = 1/x
    ln = sum(x[::2])-sum(x[1::2])
    return ln

ln2 = alt_harmonic(5000) # put your approximation for ln(2) here
print ln2

