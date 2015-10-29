# spec.py
"""Volume II Lab 8: Markov Chains
Donald Rex  
Hello
Math
"""
import numpy as np


# Problem 1: implement this function.
def random_markov(n):
    """Create and return a transition matrix for a random
    Markov chain with 'n' states as an nxn NumPy array.
    """
    markov = np.random.uniform(0,5,size=(n,n)) 
    for i in xrange(n):
        markov[:,i] /= np.sum(markov[:,i])
    return markov

# Problem 2: modify this function.
def forecast(num_days):
    """Run a simulation for the weather over 'num_days' days, with
    "hot" as the starting state. Return a list containing the day-by-day
    results, not including the starting day.

    Example:
        >>> forecast(5)
        [1, 0, 0, 1, 0]
        # Or, if you prefer,
        ['cold', 'hot', 'hot', 'cold', 'hot']
    """
    state = 0
    markov = np.array([[.7,.6],[.3,.4]])
    chain = []
    for i in xrange(num_days):
        randy = np.random.random()
        if state == 0:
            if randy < markov[1,0]:
                state = 1
                chain.append(1)
            else:
                chain.append(0)
        else:
            if randy < markov[1,1]:
                chain.append(1)
            else:
                chain.append(0)
                state = 0
    return chain



# Problem 3: implement this function.
def four_state_forecast(days=1):
    """Same as forecast(), but using the four-state transition matrix."""
    markov = np.array([[.5,.3,.1,0],
                        [.3,.3,.3,.3],
                        [.2,.3,.4,.5],
                        [0,.1,.2,.2]])
    state = 0
    chain = []
    for i in xrange(days):
        probs = markov[:,state]
        draw = np.random.multinomial(1,probs)
        state = np.argmax(draw)
        chain.append(state)
    return chain


# Problem 4: implement this function.
def analyze_simulation():
    """Analyze the results of the previous two problems. What percentage
    of days are in each state? Print your results to the terminal.
    """
    chain = four_state_forecast(10000)
    print("Hot days", chain.count(0)/10000.)
    print("Mild days", chain.count(1)/10000.)
    print("Cold days", chain.count(2)/10000.)
    print("Freezing days", chain.count(3)/10000.)
    pass

# Problems 5-6: define and implement the described functions.
f = open('gb.txt','r')
contents = f.readlines()
wordbank = dict()
i = 0
for line in contents:
     words = line.split()
     for word in words:
         if word not in a:
             wordbank
     

print contents
# Problem 7: implement this function.
def sentences(infile, outfile, num_sentences=1):
    """Generate random sentences using the word list generated in
    Problem 5 and the transition matrix generated in Problem 6.
    Write the results to the specified outfile.

    Parameters:
        infile (str): The path to a filen containing a training set.
        outfile (str): The file to write the random sentences to.
        num_sentences (int): The number of random sentences to write.

    Returns:
        None
    """
    raise NotImplementedError("Problem 7 incomplete.")
