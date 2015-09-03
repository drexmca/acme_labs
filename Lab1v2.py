import sys
import csv
import math
import cmath
import random 
from collections import namedtuple 
from collections import deque
import itertools
import timeit
import numpy as np

###### Problem 2 #####
# Prints out an argument from the sys.argv
# a = sys.argv
# print a[1]


###### Problem 3 ######
# open test.csv as read-only
def printtributes():
    male_list = []
    female_list = []
    with open('tributes.csv', 'r') as csv_file:
        tributes = csv.reader(csv_file)
        for male, female in tributes:
            male_list.append(male)
            female_list.append(female)
        return male_list, female_list
    
males, females = printtributes()
print (males)
print (females)

print ("Press any key to continue")
raw_input()


#### Problem 4 ####
def root(n):
    try: root = math.sqrt(n)
    except ValueError:
        root = cmath.sqrt(n)
    except TypeError:
        root = None
    return root

print (root(5))
print (root(-5))
print ("Press any key to continue")
raw_input()

#### Problem 5 ####

rand = [random.uniform(0.,10.) for i in range(0,24)]
print rand

print ("Press any key to continue")
raw_input()

#### Problem 6 ####
class Tribclass(tuple):
 
    def __init__(self, district, name, gender):
        self.district = district
        self.name = name
        self.gender = gender

Tribute = namedtuple("Tribclass", ['name', 'district', 'gender'])

def tribute(tributes):
    for d, t in enumerate(itertools.izip(males, females),1):
        tributes.append(Tribute(t[0], d, 'M'))
        tributes.append(Tribute(t[1], d, 'F'))
    return tributes


A =tribute([])
#print (A[0])

#### Problem 7 ####

def roatate_list_num(lst):
    """
    I built this one, though I admit it has no for loops, and only works 
    on lists of numbers. It's cool though)
    """
    return lst[len(lst)-1:]+lst[:len(lst)-1]

def rotate_list(lst, n):
    for i in range(n):
        item = lst[len(lst)-1]
        lst.pop(len(lst)-1)
        lst.insert(0,item)

def rotate_deque(d,n):
    d = d.rotate(n)

def time_func(f, args =(), repeat = 3, number = 100):
    pfunc = lambda: f(*args)
    T = timeit.Timer(pfunc)
    try:
        t = T.repeat(repeat=repeat, number=int(number))
        runtime = min(t)/float(number)
        return runtime
    except:
        T.print_exc()

d = deque(range(10000))

lst = list(range(10000))


#print (time_func(rotate_deque, (d, 10000)))
#print ("Wait for it, it could take a while")
#print (time_func(rotate_list, (lst, 10000)))


#### Problem 8 ####
event_list= []
with open("events.txt", 'r') as f:
    event = csv.reader(f)
    for line in event:
        event_list.append(line)

print len(event_list)
a = random.randint(0,40)
b = random.randint(0,40)
c = random.randint(0,40)
d = random.randint(0,40)

#print event_list[a],event_list[b],event_list[c],event_list[d]
def survival(num):
    survive = []
    for i in range(num):
        survive.append((random.random()*9+1))
    return survive
    
def HungerSim(tributes, events, prob): 
    """
    Parameters are: 
    events - list of events from Problem 1. 
    likelihoods - the list of random numbers from Problem 5. 
    tributes - the list of tributes from Problem 6
    """
    day = 1
    with open("output.txt", 'w') as f:
        while len(tributes)>1:
            f.write("Day"+str(day)+"\n")
            day = day + 1
            event_prob = []
            survivors = []

            for d in range(41):
                event_prob.append(random.uniform(1.0,10.0))


            for i,x in enumerate(tributes):
                tribute_event = random.randint(0,40)
                y = event_prob[tribute_event]
                if prob[i] < y:
                    f.writelines([tributes[i].name," from District ", 
                        str(tributes[i].district)," experienced ", 
                        str(events[tribute_event]), " and died\n"])
                    del tributes[i]

                else:
                    f.writelines([tributes[i].name, " from District ", 
                        str(tributes[i].district), " experienced ",
                        str(events[tribute_event]), " and survived\n"])

                del prob

                prob = []
                
                for i in range(len(tributes)):
                    prob.append(random.uniform(1.0, 10.0))

        if len(tributes) ==1:
            f.write(tributes[0].name + " from District " +
                    str(tributes[0].district) + " Won")
        else:
            f.write("No one survived")

HungerSim(A, event_list, rand)
