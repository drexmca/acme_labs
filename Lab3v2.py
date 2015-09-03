import numpy as np
from numpy.linalg import norm
from scipy.sparse import linalg as la
from matplotlib import pyplot as plt

#### Problem 1 ####
#Functions given in set
class Node(object):
    def __init__(self, data):
        self.next = None
        self.value = data

class SLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __len__(self):
        return self.size

    def find(self, index):
        if index >= len(self):
            raise IndexError

        nfind = self.head
        nprev = None
        count = 0

        while count < index and nfind.next:
            count += 1
            nprev = nfind
            nfind = nfind.next
        return nprev, nfind


    def insert(self, index, data):
        if index > len(self):
            raise IndexError

        n = Node(data)
        if index == 0:
            n.next = self.head
            self.head = n
            if len(self) == 0:
                self.tail = self.head

        elif index == len(self):
            self.tail.next = n
            self.tail = n

        else:
            nprev, nindex = self.find(index)
            n.next = nindex
            nprev.next = n
        self.size += 1

    def clear(self):
        self.head = None

    def __str__(self):
        return '[' + ','.join(map(str, iter(self))) + ']'

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.value
            temp = temp.next

# Define a Remove function here

def remove(self, index):
    """
    This function handles all of the different possibilities, when the
    index is too big, =0, and the last element. It then tells it what
    to do in each case.
    """
    if index>= len(self):
        raise IndexError

    if index == 0:
        self.head = self.nead.next

    elif index == len(self)-1:
        nprev, nlast = self.find(index)
        nprev.next = None
        self.tail = nprev

    else:
        nprev, nindex = self.find(index)
        nprev.next = nindex.next
    self.size -= 1


### Problem 2 ### 

#given functions
class Node(object):
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self,data):
        def _recur_insert(node, item):
            if node is None:
                return Node(item)
            else:

                if item < node.value:
                    node.left = _recur_insert(node.left, item)
                elif item > node.value:
                    node.right = _recur_insert(node.right, item)
            return node

        self.root = _recur_insert(self.root, data)
        self.size += 1

#written functions

        def find(self, data):
            def _recur_find(node, item):
                if node.value == item:
                    return node
                elif node.value > item:
                    if node.left is None:
                        return False
                    else:
                        return _recur_find(node.left,item)
                else:
                    if node.right is None:
                        return False
                    else:
                        return _recur_find(node.right,item)

        return _recur_find(self.root, data)


### Problem 3 ###
    def remove(self, item):
        def _recur_remove(n, cand):

            if n is None:
                # Nothing is done, if the node is None.
                return
            else:
                # Otherwise if the node isn't None...
                if cand < n.value:
                   # If candidate is less than the node's value... 
                    n.left = _recur_remove(n.left, cand)
                    # Check the left side
                elif cand > n.value:
                    # If candidate is greater
                    n.right = _recur_remove(n.right, cand)
                    # Check the right side
                elif cand == n.value:
                    # If they are equal
                    if n.left is None and n.right is None:
                        # remove it
                        return
                elif n.left is not None and n.right is None:
                    # If node only has left child... do this
                    nleft = n.left
                    del n
                    return nleft
                elif n.left is None and n.right is not None:
                    # If node only has right child... do this
                    nright = n.right
                    del n
                    return nright
                else:
                    # This is done if the node has two children, find
                    # The min value
                    nmin = n.right
                    while nmin.left is not None:
                        #Finds the min value inside of the left tree
                        nmin = nmin.left
                    n.value, nmin.value = nmin.value, n.value
                    # Switches the parent node with the min value
                    n.right = _recur_remove(n.right, nmin.value)
                    return n
                return n
        if self.root is None:
            # If tree is empty nothing is done.
            return
        else:
            self.root = _recur_remove(self.root, item)
            #Takes one away from the size 
        self.size -= 1

## Problem 4 ##
class HashTable(object):
	def __init__(self, capacity):
		self.hashtable= [list() for i in xrange(capacity)]
		self.size = 0
		self.capacity = capacity

	def load_factor(self):
		return float(self.size)/self.capacity

	def insert(self, data):
		if self.load_factor() < 1:
			self.hashtable[hash(data) % self.capacity].append(data)
		self.size += 1

	def resize(self, new_cap=0):
		if new_cap != 0: 
			new_table = HashTable(new_cap)

		else:  
			if self.load_factor() > 0.8:
				new_table=self
				size = self.size 

				while new_table.load_factor() >= 0.3:
					new_cap = new_table.capacity 
					new_cap *= 2 

					new_table = HashTable(new_cap)
					new_table.size = size

			else:
				print 'Not changed. Not over .8.'
				return self
		
				
		for i in xrange(len(self.hashtable)):
			for j in self.hashtable[i]:
				new_table.hashtable[hash(j) % new_table.capacity].append(j)
		return new_table
		

table=HashTable(4)

animals= ['lion', 'tiger', 'cheetah', 'cougar', 'colocolo','cat', 'clouded leopard', 'jaguar']
for i in animals:
	if table.load_factor() < 0.8:
		table.insert(i)
	else:
		table=table.resize()
		table.insert(i)

print table.hashtable




