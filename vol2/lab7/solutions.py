# spec.py
"""Volume II Lab 7: Breadth-First Search (Kevin Bacon)
Donald Rex McArthur
Math 321
Oct 20, 2013
"""
from collections import deque 
import networkx as nx
from matplotlib import pyplot as plt

# Problems 1-4: Implement the following class
class Graph(object):
    """A graph object, stored as an adjacency dictionary. Each node in the
    graph is a key in the dictionary. The value of each key is a list of the
    corresponding node's neighbors.

    Attributes:
        dictionary: the adjacency list of the graph.
    """

    def __init__(self, adjacency):
        """Store the adjacency dictionary as a class attribute."""
        self.dictionary = adjacency

    # Problem 1
    def __str__(self):
        """String representation: a sorted view of the adjacency dictionary.
        
        Example:
            >>> test = {'A':['B'], 'B':['A', 'C',], 'C':['B']}
            >>> print(Graph(test))
            A: B
            B: A; C
            C: B
        """
        A = str()
        for i in sorted(self.dictionary.keys()):
            A += (i) + ': ' 
            A += ' ,'.join(test[i]) + '\n'
        return A


    # Problem 2
    def traverse(self, start):
        """Begin at 'start' and perform a breadth-first search until all
        nodes in the graph have been visited. Return a list of values,
        in the order that they were visited.

        Inputs:
            start: the node to start the search at.

        Returns:
            the list of visited nodes (in order of visitation).

        Raises:
            ValueError: if 'start' is not in the adjacency dictionary.

        Example:
            >>> test = {'A':['B'], 'B':['A', 'C',], 'C':['B']}
            >>> Graph(test).traverse('B')
            ['B', 'A', 'C']
        """
        if start in self.dictionary:
            current = start
            marked = set()
            visited = list()
            visit_queue = deque()

            visit_queue.append(current) 
            while len(visit_queue) > 0:
                current = visit_queue.popleft()
                visited.append(current)
                marked.add(current)
                for neighbor in self.dictionary[current]:
                    if neighbor not in marked:
                        visit_queue.append(neighbor)
                        marked.add(neighbor)
                #print 'current: ', current
                #print 'visit queue: ', visit_queue
                #print 'marked: ', marked
                #print 'visited: ', visited
        else:
            raise ValueError("Start value is not in the dictioanry")
        return visited

    # Problem 3 (Optional)
    def DFS(self, start):
        """Begin at 'start' and perform a depth-first search until all
        nodes in the graph have been visited. Return a list of values,
        in the order that they were visited. If 'start' is not in the
        adjacency dictionary, raise a ValueError.

        Inputs:
            start: the node to start the search at.

        Returns:
            the list of visited nodes (in order of visitation)
        """
        raise NotImplementedError("Problem 3 Incomplete")

    # Problem 4
    def shortest_path(self, start, target):
        """Begin at the node containing 'start' and perform a breadth-first
        search until the node containing 'target' is found. Return a list
        containg the shortest path from 'start' to 'target'. If either of
        the inputs are not in the adjacency graph, raise a ValueError.

        Inputs:
            start: the node to start the search at.
            target: the node to search for.

        Returns:
            A list of nodes along the shortest path from start to target,
                including the endpoints.

        Example:
            >>> test = {'A':['B', 'F'], 'B':['A', 'C'], 'C':['B', 'D'],
            ...         'D':['C', 'E'], 'E':['D', 'F'], 'F':['A', 'E', 'G'],
            ...         'G':['A', 'F']}
            >>> Graph(test).shortest_path('A', 'G')
            ['A', 'F', 'G']
        """
        path = {}
        #print start in self.dictionary
        #print target in self.dictionary
        if start in self.dictionary and target in self.dictionary:
            current = start
            marked = set()
            visited = []
            visit_queue = deque()

            visit_queue.append(current) 
            while target != current:
                visited.append(current)
                marked.add(current)
                for neighbor in self.dictionary[current]:
                    if neighbor not in marked:
                        visit_queue.append(neighbor)
                        path[current] = neighbor
                        marked.add(neighbor)
                current = visit_queue.popleft()
                
                #print 'current: ', current
                #print 'visit queue: ', visit_queue
                #print 'marked: ', marked
                #print 'visited: ', visited
            short = []
            current = start
            short.append(current)
            while current != target:
                short.append(path[current])
                current = path[current]
        else: 
            raise ValueError('Start or Target value not in dictionary')
        return short 

case1 = {'A':['B'], 'B':['A', 'C','D', 'E'], 'C':['B'],'D':['B','E'],'E':['D', 'B']}
test = Graph(case1)
total_path = test.traverse('C')
short_path = test.shortest_path('C', 'E')
print short_path

# Problem 5: Write the following function
def convert_to_networkx(dictionary):
    """Convert 'dictionary' to a networkX object and return it."""
    nx_graph = nx.Graph()
    for key in dictionary:
        for value in dictionary[key]:
            nx_graph.add_edge(key, value)
    return nx_graph
nx_graph = convert_to_networkx(case1)
nx.draw(nx_graph)
plt.show()


# Helper function for problem 6
def parse(filename="movieData.txt"):
    """Generate an adjacency dictionary where each key is
    a movie and each value is a list of actors in the movie.
    """

    # open the file, read it in, and split the text by '\n'
    with open(filename, 'r') as movieFile:
        moviesList = movieFile.read().split('\n')
    graph = dict()

    # for each movie in the file,
    for movie in moviesList:
        # get movie name and list of actors
        names = movie.split('/')
        title = names[0]
        graph[title] = []
        # add the actors to the dictionary
        for actor in names[1:]:
            graph[title].append(actor)
    
    return graph


# Problems 6-8: Implement the following class
class BaconSolver(object):
    """Class for solving the Kevin Bacon problem."""

    # Problem 6
    def __init__(self, filename="movieData.txt"):
        """Initialize the networkX graph and with data from the specified
        file. Store the graph as a class attribute. Also store the collection
        of actors in the file as an attribute.
        """
        raise NotImplementedError("Problem 6 Incomplete")

    # Problem 6
    def path_to_bacon(self, start, target="Bacon, Kevin"):
        """Find the shortest path from 'start' to 'target'."""
        raise NotImplementedError("Problem 6 Incomplete")

    # Problem 7
    def bacon_number(self, start, target="Bacon, Kevin"):
        """Return the Bacon number of 'start'."""
        raise NotImplementedError("Problem 7 Incomplete")

    # Problem 7
    def average_bacon(self, target="Bacon, Kevin"):
        """Calculate the average Bacon number in the data set.
        Note that actors are not guaranteed to be connected to the target.

        Inputs:
            target (str): the node to search the graph for
        """
        raise NotImplementedError("Problem 7 Incomplete")

# =========================== END OF FILE =============================== #
