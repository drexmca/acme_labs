# name this file 'solutions.py'
"""Volume II Lab 5: Data Structures II (Trees)
Rex McArthur
"""
from LinkedLists import LinkedList
from Trees import BST
from Trees import AVL
from WordList import create_word_list
from time import time
from matplotlib import pyplot as plt
import numpy as np

def iterative_search(linkedlist, data):
    """Find the node containing 'data' using an iterative approach.
    If there is no such node in the list, or if the list is empty,
    raise a ValueError with error message "<data> is not in the list."
    
    Inputs:
        linkedlist (LinkedList): a linked list object
        data: the data to find in the list.
    
    Returns:
        The node in 'linkedlist' containing 'data'.
    """
    # Start the search at the head.
    current = linkedlist.head
    
    # Iterate through the list, checking the data of each node.
    while current is not None:
        if current.data == data:
            return current
        current = current.next
    
    # If 'current' no longer points to a Node, raise a value error.
    raise ValueError(str(data) + " is not in the list.")


# Problem 1: rewrite iterative_search() using recursion.
def recursive_search(linkedlist, data):
    """Find the node containing 'data' using a recursive approach.
    If there is no such node in the list, raise a ValueError with error
    message "<data> is not in the list."
    
    Inputs:
        linkedlist (LinkedList): a linked list object
        data: the data to find in the list.
    
    Returns:
        The node in 'linkedlist' containing 'data'.
    """
    if linkedlist.head is None:
        raise ValueError(str(data) + " is not in the list.")
    current = linkedlist.head
    if current.data == data:
        return current
    else:
        linkedlist.remove(current.data)
        return recursive_search(linkedlist, data)

def test1():
    L = LinkedList()
    #recursive_search(L,1)
    L.add(1)
    L.add(2)
    L.add(3)
    L.add(4)
    recursive_search(L,1)
    iterative_search(L,1)
    print L
#test1()

# Problem 2: Implement BST.insert() in Trees.py.
def test2():
    B = BST()
    B.insert(4)
    B.insert(3)
    B.insert(6)
    B.insert(5)
    B.insert(7)
    B.insert(8)
    B.insert(1)
    print B
#test2()

# Problem 3: Implement BST.remove() in Trees.py
def test3():
    B = BST()
    B.insert(4)
    B.insert(3)
    B.insert(6)
    B.insert(5)
    B.insert(7)
    B.insert(8)
    B.insert(1)
    print B

    B.remove(6)
    print B

    C = BST()
    C.insert(5)
    C.insert(2)
    C.insert(9)
    C.insert(1)
    C.insert(4)
    C.insert(3)
    print C
    C.remove(2)
    print C

    D = BST()
    D.insert(1)
    D.insert(2)
    D.insert(3)
    D.insert(4)
    D.insert(5)
    D.insert(6)
    print D
    D.remove(1)
    print D
test3()

# Problem 4: Test build and search speeds for LinkedList, BST, and AVL objects.
def plot_times(filename="English.txt", start=500, stop=5500, step=500):
    """Vary n from 'start' to 'stop', incrementing by 'step'. At each
    iteration, use the create_word_list() from the 'WordList' module to
    generate a list of n randomized words from the specified file.
    
    Time (separately) how long it takes to load a LinkedList, a BST, and
    an AVL with the data set.
    
    Choose 5 random words from the data set. Time how long it takes to
    find each word in each object. Calculate the average search time for
    each object.
    
    Create one plot with two subplots. In the first subplot, plot the
    number of words in each dataset against the build time for each object.
    In the second subplot, plot the number of words against the search time
    for each object.
    
    Inputs:
        filename (str): the file to use in creating the data sets.
        start (int): the lower bound on the sample interval.
        stop (int): the upper bound on the sample interval.
        step (int): the space between points in the sample interval.
    
    Returns:
        Show the plot, but do not return any values.
    """
    interval = (stop-start)/step
    n_list = np.linspace(start,stop,interval+1)
    n_list = np.int16(n_list)
    

    word_list = create_word_list(filename)
    
    load_list = []
    load_BST = []
    load_AVL = []
    
    find_list = []
    find_BST = []
    find_AVL = []
    
    for n in n_list:
        temp_word_list = word_list[:n]
        random_word_indices = np.random.randint(0,n,size=5)
        words_to_find = []
        for x in random_word_indices:
            words_to_find.append(temp_word_list[x])

        L = LinkedList()
        B = BST()
        A = AVL()
        
        start = time()
        for word in temp_word_list:
            L.add(word)
        end = time()
        load_list.append(end-start)

        start = time()
        for word in temp_word_list:
            B.insert(word)
        end = time()
        load_BST.append(end-start)

        start = time()
        for word in temp_word_list:
            A.insert(word)
        end = time()
        load_AVL.append(end-start)
        
        start = time()
        for word in words_to_find:
            iterative_search(L, word)
        end = time()
        find_list.append(end-start)

        start = time()
        for word in words_to_find:
            B.find(word)
        end = time()
        find_BST.append(end-start)

        start = time()
        for word in words_to_find:
            A.find(word)
        end = time()
        find_AVL.append(end-start)
    
    avg_find_list = sum(find_list[:])/5.
    avg_find_BST = sum(find_BST[:])/5.
    avg_find_AVL = sum(find_AVL[:])/5.

    plt.subplot(121)
    list_plot1 = plt.plot(n_list, load_list,label='Singly-Linked List')
    BST_plot1 = plt.plot(n_list, load_BST, label='Binary Search Tree')
    AVL_plot1 = plt.plot(n_list, load_AVL, label='AVL Tree')
    plt.legend()
    plt.xlabel('Data Points')
    plt.ylabel('Seconds')
    plt.title('Build Times')

    plt.subplot(122)
    list_plot2 = plt.plot(n_list, find_list,label='Singly-Linked List')
    BST_plot2 = plt.plot(n_list, find_BST, label='Binary Search Tree')
    AVL_plot2 = plt.plot(n_list, find_AVL, label='AVL Tree')
    plt.legend()
    plt.xlabel('Data Points')
    plt.ylabel('Seconds')
    plt.title('Search Times')

    plt.show() 


#plot_times()
        
"""
If the data were sorted to begin with then the build times should be comparable for each of the
data structures used.
"""

# =============================== END OF FILE =============================== #
