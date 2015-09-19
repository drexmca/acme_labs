import numpy as np

def max_element(seq):
    '''
    Assuming length is > 2
    '''
    a = len(seq)
    if a == 1:
        return seq[0]
    if a == 2:
        return max(seq[0], seq[1])
    half = (a/2)
    if seq[half] < seq[half+1]:
        newseq = max_element(seq[half:])
        return newseq
    elif seq[half] > seq[half+1]:
        newseq = max_element(seq[:half+1])
        return newseq
    elif seq[half] == seq[half+1]:
        raise ValueError("Thou shalt not be equal")
        return 0


A = np.linspace(1,100,100)
B = np.linspace(101,51,51)
C = np.append(A,B)
print max_element(C)
