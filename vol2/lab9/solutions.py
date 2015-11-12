# name this file solutions.py
"""Volume II Lab 9: Discrete Fourier Transform
Donald Rex McArthur
Class 345

"""
import numpy as np
from scipy.io import wavfile
import os
from matplotlib import pyplot as plt



# Modify this class for problems 1, 2, 4, and 5.
class Signal(object):
    def __init__(self, rate, wave):
        self.rate = rate
        self.wave = wave

    def plot(self, DFT=False):
        if DFT:
            print self.wave
            plt.plot(self.wave)
            plt.show()

        else:
            self.wave = abs(self.wave)
            plt.plot(self.wave)
            plt.show()

    def write_file(self, filename):
        sample = self.wave*32767./np.amax(self.wave)
        sample = np.int16(sample)
        wavfile.write(filename + '.wav', self.rate, sample)

def test1():
    rate, wave = wavfile.read('tada.wav')
    tada = Signal(rate, wave)
    tada.plot()



#def gen(multiple = 1, duration = .8,framerate = 44100):
#        """Tone generator, produces multiples of middle C (C4=261.63 Hz)
#        """
#           t = np.linspace(0,duration,framerate*duration)  #time, scaled to match standard sampling rates
#           return np.sin(2*np.pi*(261.63)*t * multiple)    #sine-wave tone  
#   



# Problem 3: Implement this function.
def generate_note(frequency=440., duration=5., rate=44100.):
    """Return an instance of the Signal class corresponding to the desired
    soundwave. Sample at a rate of 44100 samples per second.
    """
    t = np.linspace(0,duration,rate*duration)
    wave = np.sin(2*np.pi*(frequency)*t)
    note = Signal(rate, wave) 
    note.write_file('note')
    return wave
    
def test2():
    A = generate_note(440, 3.)
    return A

A = test2()

# Problem 4: Implement this function.
def DFT(samples):
    """Calculated the DFT of the given array of samples."""
    c = []
    for k in xrange(len(samples)):
        c_k = []
        for n in xrange(len(samples)):
            var = samples[n] * np.exp((-2*np.pi*1j*n*k)/float(len(samples)))
            c_k = np.append(c_k, var)
            c_k = np.sum(c_k)

        c.append(c_k)
    return c
A_440 = DFT(A)
A_440 = Signal(44100., A)
A_440.plot(True)

# Problem 6: Implement this function.
def generate_chord():
    """Write a chord to a new file, 'chord1.wav'. Write a chord that changes
    over time to a new file, 'chord2.wav'.
    """
    pass
