# name this file solutions.py
"""Volume II Lab 6: Nearest Neighbor Search
Donald Rex McArthur
Math
October 17th
"""
from sklearn import neighbors
from Trees import BST
from Trees import BSTNode
import numpy as np
from scipy.spatial import KDTree
from scipy import spatial


# Problem 1: Implement this function.
def euclidean_metric(x, y):
    """Return the euclidean distance between the vectors 'x' and 'y'.

    Raises:
        ValueError: if the two vectors 'x' and 'y' are of different lengths.
    
    Example:
        >>> print(euclidean_metric([1,2],[2,2]))
        1.0
        >>> print(euclidean_metric([1,2,1],[2,2]))
        ValueError: Incompatible dimensions.
    """
    if x.shape != y.shape:
        raise ValueError(" Incompatiable dimensions")
    else:
        return spatial.distance.euclidean(x,y)


# Problem 2: Implement this function.
def exhaustive_search(data_set, target):
    """Solve the nearest neighbor search problem exhaustively.
    Check the distances between 'target' and each point in 'data_set'.
    Use the Euclidean metric to calculate distances.
    
    Inputs:
        data_set (mxk ndarray): An array of m k-dimensional points.
        target (1xk ndarray): A k-dimensional point to compare to 'dataset'.
        
    Returns:
        the member of 'data_set' that is nearest to 'target' (1xk ndarray).
        The distance from the nearest neighbor to 'target' (float).
    """
    m,k = K.shape
    distances = np.array([])
    for i in xrange(m):
        distances = np.append(distances, euclidean_metric(target,data_set[i]))
    a = np.argmin(distances)
    return data_set[a], distances[a]


a = np.array([2,4,5])
b = np.array([0,1,1])
c = np.array([-5,2,-1])
d = np.array([-5,1,-1])

K = np.vstack((a,b,c,d))
print exhaustive_search(K,np.array([1,1,1]))

# Problem 3: Finish implementing this class by modifying __init__()
#   and adding the __sub__, __eq__, __lt__, and __gt__ magic methods.
class KDTNode(BSTNode):
    """Node class for K-D Trees. Inherits from BSTNode.

    Attributes:
        left (KDTNode): a reference to this node's left child.
        right (KDTNode): a reference to this node's right child.
        parent (KDTNode): a reference to this node's parent node.
        data (ndarray): a coordinate in k-dimensional space.
        axis (int): the 'dimension' of the node to make comparisons on.
    """

    def __init__(self, data):
        """Construct a K-D Tree node containing 'data'. The left, right,
        and prev attributes are set in the constructor of BSTNode.

        Raises:
            TypeError: if 'data' is not a a numpy array (of type np.ndarray).
        """
        if type(data) is np.ndarray:
            BSTNode.__init__(self, data)
            self.axis  = 0
        else:
            raise TypeError('Data not NP array')
    
    def __sub__(self, other):
        return euclidean_metric(self.data,other.data)

    def __eq__(self, other):
        return np.allclose(self.data,other.data)
    
    def __lt__(self, other):
        axis = other.axis
        return self.data[axis] < other.data[axis]

    def __gt__(self,other):
        axis = other.axis
        return self.data[axis] > other.data[axis]

data = np.array([1.,2.])
data1 = np.array([2.,0])
a = KDTNode(data)
b = KDTNode(data1)
a.axis = 1
print b < a
print b-a

# Problem 4: Finish implementing this class by overriding
#   the insert() and remove() methods.
class KDT(BST):
    """A k-dimensional binary search tree object.
    Used to solve the nearest neighbor problem efficiently.

    Attributes:
        root (KDTNode): the root node of the tree. Like all other
            nodes in the tree, the root houses data as a numpy array.
        k (int): the dimension of the tree (the 'k' of the k-d tree).
    """
    
    def find(self, data):
        """Return the node containing 'data'.

        Raises:
            ValueError: if there is node containing 'data' in the tree,
                or the tree is empty.
        """

        # First check that the tree is not empty.
        if self.root is None:
            raise ValueError(str(data) + " is not in the tree.")
        
        # Define a recursive function to traverse the tree.
        def _step(current, target):
            """Recursively approach the target node."""
            
            if current is None:             # Base case: target not found.
                return current
            if current == other:            # Base case: target found!
                return current
            if target < current:            # Recursively search to the left.
                return _step(current.left, target)
            else:                           # Recursively search to the right.
                return _step(current.right, target)
            
        # Create a new node to use the KDTNode comparison operators.
        n = KDTNode(data)

        # Call the recursive function, starting at the root.
        found = _step(self.root, n)
        if found is None:                  # Report the data was not found.
            raise ValueError(str(data) + " is not in the tree.")
        return found                       # Otherwise, return the target node.

    
    def insert(self, data):

        def traverse(current, target):

            if target < current:
                if current.left is None:
                    current.left = target
                    target.axis = (current.axis +1) % current.data.shape[0]
                else:
                    traverse(current.left, target)
            if target > current:
                if current.right is None:
                    current.right = target
                    target.axis = (current.axis +1) % current.data.shape[0]
                else:
                    traverse(current.right, target)

        n = KDTNode(data)
        if self.root is None:
            self.root = n
        else: 
            traverse(self.root, n)
    
    def remove(*args):
        raise NotImplementedError("Sorry, don't want you to do that")

data_set = np.array([[1, -9, -9,-2],
                    [100, 5, 4, 3],
                    [2,   2, 5, 6],
                    [-52, 8, 1, 7],
                    [5,   4, 32,-3]])

A = KDT()
for i in xrange(data_set.shape[0]):
    A.insert(data_set[i])
print A
'subtraction'
print A.root.right - A.root
        

# Problem 5: Implement this function.
def KDTSearch(current, target, neighbor, distance):
    if current is None:
        return neighbor, distance
    index = current.axis

    if current - target < distance:
        neighbor = current
        distance = current - target

    if target.data[index] < current.data[index]:
        neighbor, distance = KDTSearch(current.left, target, neighbor, distance)
        if target.data[index] + distance >= current.data[index]:
            neighbor, distance = KDTSearch(current.right, 
                    target, neighbor, distance)

    else:
        neighbor, distance = KDTSearch(current.right, target, neighbor, distance)
        if target.data[index] - distance <= current.data[index]:
            neighbor, distance = KDTSearch(current.left,
                    target, neighbor, distance)
    return neighbor, distance

def nearest_neighbor(data_set, target):
    """Use the KDT class to solve the nearest neighbor problem.

    Inputs:
        data_set (mxk ndarray): An array of m k-dimensional points.
        target (1xk ndarray): A k-dimensional point to compare to 'dataset'.

    Returns:
        The point in the tree that is nearest to 'target' (1xk ndarray).
        The distance from the nearest neighbor to 'target' (float).
    """
    A = KDT()
    for i in xrange(data_set.shape[0]):
        A.insert(data_set[i])

    return KDTSearch(A.root, KDTNode(target), A.root, A.root-KDTNode(target))

data_set = np.array([[1,-9,-9,-2],
                    [100,5,4,3],
                    [2,2,5,6],
                    [-52,8,1,7],
                    [5,4,32,-3]])

a,b = nearest_neighbor(data_set,np.array([2,2,5,4]))
print a 
print  b

# Problem 6: Implement this function.
def postal_problem():
    """Use the neighbors module in sklearn to classify the Postal data set
    provided in 'PostalData.npz'. Classify the testpoints with 'n_neighbors'
    as 1, 4, or 10, and with 'weights' as 'uniform' or 'distance'. For each
    trial print a report indicating how the classifier performs in terms of
    percentage of misclassifications.

    Your function should print a report similar to the following:
    n_neighbors = 1, weights = 'distance':  0.903
    n_neighbors = 1, weights =  'uniform':  0.903       (...and so on.)
    """
    labels, points, testlabels, testpoints = np.load("PostalData.npz").items()
    def calcpoints(n,dist):
        nbrs = neighbors.KNeighborsClassifier(n_neighbors=n, weights=dist, p=2)
        nbrs.fit(points[1], labels[1])
        prediction = nbrs.predict(testpoints[1])
        average = np.average(prediction/testlabels[1])
        print 'n_neighbors = ' + str(n) +', weights = ' + dist + str(average)
    calcpoints(1, 'uniform')
    calcpoints(1, 'distance')
    calcpoints(4, 'distance')
    calcpoints(4, 'uniform')
    calcpoints(10, 'distance')
    calcpoints(10, 'uniform')

postal_problem()



# =============================== END OF FILE =============================== #
