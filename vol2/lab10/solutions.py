# Name this file solutions.py.
"""Volume II Lab 10: Fourier II (Filtering and Convolution)
Donald Rex McArthur
Math 321
Nov...
"""
from scipy.io import wavfile
import numpy as np
import lab9
# Problem 1: Implement this function.
def clean_signal(outfile='prob1.wav'):
    """Clean the 'Noisysignal2.wav' file. Plot the resulting sound
    wave and write the resulting sound to the specified outfile.
    """
    rate, data = wavfile.read('Noisysignal2.wav')
    fsig = np.fft.fft(data)
    for j in xrange(150000,200000):
        fsig[j]=0
        fsig[-j]=0
    newsig = np.fft.ifft(fsig)
    newsig = np.real(fsig)
    newsig = np.int16(newsig/np.abs(newsig).max()*32767)
    clear = lab9.Signal(rate,newsig)
    clear.write_file(outfile)
    pass
    
def test1():
    clean_signal()
test1()


# Problem 2 is not required. Use balloon.wav for problem 3.

# Problem 3: Implement this function.
def convolve(source='chopin.wav', pulse='balloon.wav', outfile='prob3.wav'):
    """Convolve the specified source file with the specified pulse file, then
    write the resulting sound wave to the specified outfile.
    """
    raise NotImplementedError("Problem 3 Incomplete.")

# Problem 4: Implement this function.
def white_noise(outfile='prob4.wav'):
    """Generate some white noise, write it to the specified outfile,
    and plot the spectrum (DFT) of the signal.
    """
    raise NotImplementedError("Problem 4 Incomplete.")
