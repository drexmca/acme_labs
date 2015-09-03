"""
I didn't do anything with this lab except check to see that it runs.  


Execrcise 1.1 float(a) or float(1)
Exercise 1.2 z=complex(1,2) or 1+2j, to return real, z.real. z.imag
Exercise 1.3 (a) 7/3 returns 2 because it is integer division, and it does the floor. So the lowest value.
To get decimal answers, use float variables, or do 7./3
To get integer answers you do 7//3
Exercise 2.1 my_string[::3] will start at the first, adn return every 3rd letter, to print backwards do, my_string[::-1]
Exercise 2.2 To get a string bookwards, just use the my_string[::-1], and it will move backwards to print the string.
Exercise 3.1
(a) len(my_list) 
(b) my_list.append("Jonathan, my pet fish")
(c) my_list.insert(3, "pizza")
(d) del my_list[:]
"""
print("Problem 3")

my_list = ["mushrooms", "rock climbing", 1947, 1954, "yoga"]
print (len(my_list))
my_list.append("Jonathan, my pet fish")
print (my_list)
my_list.insert(3,"pizza")
print (my_list)
del my_list[:]
print (my_list)
print ("Press any key to continue")
raw_input()
print("Exercise 2")
num = []
num.extend([3,5,19,20,4])
print (num)
num[3]= str(num[3])
print (num)
num.pop(2)
print (num)
num = num[::-1]
print num

print ("Press any key")
raw_input()

print ("Problem 3.3")

num = [str(x) for x in num]
print (num)

print ("Press any key")
raw_input()

"""
Problem 4
To create a set, you can either do set() or put the things in comma seperated in curly braces {'apple"}
"""


print("Problem 6") 
set1={'Apple', 'Orange', 'Banana', 'Tango'}
set2= {'Green', 'Blue', 'Banana', 'Orange'}
setunion=set1.union(set2)
print (setunion)

print ("Press only the j key")
raw_input()


"""
Problem 5
You can create a dictionary explicitly by listing
d={"Rex":21, "Dr. Evans": 40}
or using an iterable in the dict() method
d = dict([("Rex", 25), ("Dr. Evans", 40)])

to make an empty dictionary, d=dict()
Exercise 2
d.popitem()
Exercise 3
d.viewvalues()
d.viewitems()

"""
print ("Problem 6")
my_list = []
def track(n, my_list = []):
    my_list.append(n)
    return my_list

print (track(1))
print (track(2))
print (track(3))
print (track(1,[2,3,4]))
print (my_list)
print("Press any key to continue")
raw_input()
"""
Problem 7
print literally prints out what you put in the (), if you do variables, then it prints the value, string will print strings.
return returns the value of the function to be assigned to a variable
"""

grocery_list = ['pineapple', 'orange juice', 'avocados', 'pesto sauce']
for i in range (len(grocery_list)):
    if i%2 ==0:
        print (i, grocery_list[i])


