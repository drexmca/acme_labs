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
def read_file(filename):
    f = open(filename,'r')
    contents = f.readlines()
    wordbank = {}
    w = open('wordbank.txt', 'w')
    i = 1
    for line in contents:
        words = line.split()
        for word in words:
            if word not in wordbank:
                w.write(str(i)+ ' ')
                wordbank[word] = i
                i+=1
            else:
                w.write(str(wordbank[word]) + ' ')
        w.write('\n')
    inv_word = {v: k for k, v in wordbank.items()} 
    wordlist = ['$$tart']
    for i in inv_word:
        wordlist.append(inv_word[i])
    wordlist.append('#nd')
    return inv_word, wordlist


def count_words(filename):
    wordbank, wordlist = read_file(filename)
    length = len(wordlist)
    markov = np.zeros((length+2,length+2))
    f = open('wordbank.txt','r')
    contents = f.readlines()
    j = 0
    for line in contents:
        numbers = line.split()
        markov[numbers[0],0]+=1.
        if len(numbers)>1:
            for i in xrange(len(numbers)-1):
                markov[numbers[i+1], numbers[i]]+=1.
            markov[-1,numbers[i+1]]+=1.
        else:
            markov[-1,numbers[0]]+=1.
    markov /= np.sum(markov, axis=0)
    where_nans = np.isnan(markov)
    markov[where_nans] = 0
    return markov

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
    wordbank, wordlist = read_file(infile)
    markov = count_words(infile)
    song = open(outfile, 'w')
    for i in xrange(num_sentences):
        state = 0
        chain = []
        while state != len(wordlist)+1:
            probs = markov[:,state]
            draw = np.random.multinomial(1,probs)
            state = np.argmax(draw)
            chain.append(state)
        song.write(str(i+1) + ' ' + wordbank[chain[0]])
        for index in xrange(1,len(chain)-1):
            if index != len(wordlist)+1:
                song.write(' '+wordbank[chain[index]])
        song.write('.\n')







