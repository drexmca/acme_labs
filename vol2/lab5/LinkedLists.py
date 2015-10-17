# LinkedLists.py
"""Volume II Lab 4: Data Structures 1 (Linked Lists)
Auxiliary file. Modify this file for problems 1-5.
Donald Rex McArthur
Math something
Today
"""

# Problem 1: Add the magic methods __str__, __lt__, __eq__, and __gt__.
class Node(object):
    """A Node class for storing data."""
    def __init__(self, data):
        """Construct a new node that stores some data."""
        self.data = data
    def __str__(self):
        return str(self.data)

    def __lt__(self, other):
        return self.data < other.data

    def __eq__(self, other):
        return self.data == other.data

    def __gt__(self, other):
        return self.data > other.data

class LinkedListNode(Node):
    """A Node class for linked lists. Inherits from the 'Node' class.
    Contains a reference to the next node in the list.
    """
    def __init__(self, data):
        """Construct a Node and initialize an attribute for
        the next node in the list.
        """
        Node.__init__(self, data)
        self.next = None

# Problems 2-4: Finish implementing this class.
class LinkedList(object):
    """Singly-linked list data structure class.
    The first node in the list is referenced to by 'head'.
    """
    def __init__(self):
        """Create a new empty linked list. Create the head
        attribute and set it to None since the list is empty.
        """
        self.head = None

    def add(self, data):
        """Create a new Node containing 'data' and add it to
        the end of the list.
        
        Example:
            >>> my_list = LinkedList()
            >>> my_list.add(1)
            >>> my_list.head.data
            1
            >>> my_list.add(2)
            >>> my_list.head.next.data
            2
        """
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    # Problem 2: Implement the __str__ method so that a LinkedList instance can
    #   be printed out the same way that Python lists are printed.
    def __str__(self):
        """String representation: the same as a standard Python list.
        
        Example:
            >>> my_list = LinkedList()
            >>> my_list.add(1)
            >>> my_list.add(2)
            >>> my_list.add(3)
            >>> print(my_list)
            [1, 2, 3]
            >>> str(my_list) == str([1,2,3])
            True
        """
        result = []
        if self.head is None:
            return str(result)
        else:
            current_node = self.head
            result.append(current_node.data)
            while current_node.next is not None:
                current_node = current_node.next
                result.append(current_node.data)
            #result = str(result)
            return str(result)

    # Problem 3: Finish implementing LinkedList.remove() so that if the node
    #   is not found, an exception is raised.
    def remove(self, data):
        """Remove the node containing 'data'. If the list is empty, or if the
        target node is not in the list, raise a ValueError with error message
        "<data> is not in the list."
        
        Example:
            >>> print(my_list)
            [1, 2, 3]
            >>> my_list.remove(2)
            >>> print(my_list)
            [1, 3]
            >>> my_list.remove(2)
            2 is not in the list.
            >>> print(my_list)
            [1, 3]
        """
        if self.head is None:
            raise ValueError("{} is not in the list.".format(data))
        if self.head.data == data:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next.data != data:
                if current_node.next.next is None:
                    raise ValueError("{} is not in the list.".format(data))
                current_node = current_node.next
            new_next_node = current_node.next.next
            current_node.next = new_next_node
            
    # Problem 4: Implement LinkedList.insert().
    def insert(self, data, place):
        """Create a new Node containing 'data'. Insert it into the list before
        the first Node in the list containing 'place'. If the list is empty, or
        if there is no node containing 'place' in the list, raise a ValueError
        with error message "<place> is not in the list."
        
        Example:
            >>> print(my_list)
            [1, 3]
            >>> my_list.insert(2,3)
            >>> print(my_list)
            [1, 2, 3]
            >>> my_list.insert(2,4)
            4 is not in the list.
        """
        if self.head is None:
            raise ValueError("{} is not in the list.".format(place))
        if self.head.data == place:
            old_next = self.head
            new_node = LinkedListNode(data)
            new_node.next = old_next
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next.data != place:
                if current_node.next.next is None:
                    raise ValueError("{} is not in the list.".format(place))
                current_node = current_node.next
            old_next = current_node.next
            new_node = LinkedListNode(data)
            new_node.next = old_next
            current_node.next = new_node

def test24():
    L = LinkedList()
    print str(L) == str([])
    #L.remove(1)
    #L.insert(4,1)
    L.add(1)
    L.add(2)
    L.add(3)
    print(L)
    print str(L) == str([1,2,3])
    print str(L)
    L.remove(2)
    print L
    #L.remove(2)
    L.insert(4,1)
    L.insert(5,3)
    print L
#test24()


class DoublyLinkedListNode(LinkedListNode):
    """A Node class for doubly-linked lists. Inherits from the 'Node' class.
    Contains references to the next and previous nodes in the list.
    """
    def __init__(self,data):
        """Initialize the next and prev attributes."""
        Node.__init__(self,data)
        self.next = None
        self.prev = None

# Problem 5: Implement this class.
class DoublyLinkedList(LinkedList):
    """Doubly-linked list data structure class. Inherits from the 'LinkedList'
    class. Has a 'head' for the front of the list and a 'tail' for the end.
    """
    def __init__(self):
        LinkedList.__init__(self)
        self.tail = None
         
    def add(self, data):
        new_node = DoublyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            temp = current_node
            current_node.next = new_node
            new_node.next = temp.next.next
            new_node.prev = current_node
            self.tail = new_node

    def remove(self, data):
        if self.head is None:
            raise ValueError("{} is not in the list.".format(data))
        elif self.head.data == data:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next.data != data:
                if current_node.next.next is None:
                    raise ValueError("{} is not in the list.".format(data))
                current_node = current_node.next
            temp = current_node.next
            if temp.next is not None:
                current_node.next = temp.next
                current_node.next.prev = temp.prev
            elif temp.next is None:
                current_node.next = None
                self.tail = current_node

    def insert(self, data, place):
        if self.head is None:
            raise ValueError("{} is not in the list.".format(place))
        if self.head.data == place:
            new = DoublyLinkedListNode(data)
            temp = self.head
            self.head = new
            new.next = temp
        else:
            current_node = self.head
            while current_node.next.data != place:
                if current_node.next.next is None:
                    raise ValueError("{} is not in the list.".format(place))
                current_node = current_node.next
            new = DoublyLinkedListNode(data)
            temp = current_node.next
            new.prev = current_node
            current_node.next = new
            new.next = temp
            temp.prev = new

def test5():
    DL = DoublyLinkedList()
    DL.add(2)
    DL.add(4)
    DL.add(6)
    DL.add(8)
    DL.add(10)
    print DL
    print DL.head
    print DL.head.next
    print DL.head.next.next
    print DL.head.next.next.next
    print DL.head.next.next.next.next
    print DL.tail
    print DL.tail.prev
    print DL.tail.prev.prev
    print DL.tail.prev.prev.prev
    print DL.tail.prev.prev.prev.prev
    print DL
    DL.remove(10)
    print DL
    print DL.tail
    print DL.tail.prev
    print DL.head
    print "--------------------------------------"
    DL.insert(7,6)
    print DL.head
    print DL.head.next
    print DL.head.next.next
    print DL.head.next.next.next
    print DL.head.next.next.next.next

# Problem 6: Implement this class. Use an instance of your object to implement
# the sort_words() function in solutions.py.
class SortedLinkedList(DoublyLinkedList):
    """Sorted doubly-linked list data structure class."""

    # Overload add() and insert().
    def add(self, data):
        """Create a new Node containing 'data' and insert it at the
        appropriate location to preserve list sorting.
        
        Example:
            >>> print(my_list)
            [3, 5]
            >>> my_list.add(2)
            >>> my_list.add(4)
            >>> my_list.add(6)
            >>> print(my_list)
            [2, 3, 4, 5, 6]
        """
        if self.head is None:
            new = DoublyLinkedListNode(data)
            self.head = new 
            self.tail = new
        elif self.head.data >= data:
            new = DoublyLinkedListNode(data)
            temp = self.head
            self.head = new
            new.next = temp
        elif data > self.tail.data:
            new = DoublyLinkedListNode(data)
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        else:
            current_node = self.head
            while current_node.next.data <= data:
                current_node = current_node.next
            new = DoublyLinkedListNode(data)
            temp = current_node.next
            new.prev = current_node
            current_node.next = new
            new.next = temp
            temp.prev = new
    def insert(self, *args):
        raise ValueError("insert() has been disabled for this class.")

def test6():
    SL = SortedLinkedList()
    SL.add(1)
    SL.add(9)
    SL.add(-9)
    SL.add(3)
    SL.add(4)
    print SL
#test6()


# =============================== END OF FILE =============================== #
