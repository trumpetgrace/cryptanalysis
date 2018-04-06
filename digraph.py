from cryptoIO import TextToIntArray
from cryptoIO import IntArrayToText
import numpy as np
import matplotlib.pyplot as plt

def getDigraphs(ciphertext):
    ciphertext = ciphertext.lower()

    if len(ciphertext) > 300:
        freq = int(len(ciphertext)/100)
    else:
        freq = 1

    # make lists length of alphabet
    array1 = np.arange(26)
    array2 = np.arange(26)

    # n-dimensional array (array1xarray2)
    array1, array2 = np.meshgrid(array1, array2)

    # listifies array?
    array1 = array1.flatten()
    array2 = array2.flatten()

    # converts numbers to letters

    array1 = IntArrayToText(list(array1))
    array2 = IntArrayToText(list(array2))

    # turn into tuple
    tuples = np.array([(array1[i] + array2[i]) for i in range(676)])
    # print (tuples)

    length = len(ciphertext)

    digrapharray = np.array([ciphertext[i:i+2] for i in range(int(length-1))])
    # print(digrapharray)

    difreq = np.empty((676,2), dtype="object")

    for i,di in enumerate(tuples):
        difreq[i,1]=(di == digrapharray).sum()
        difreq[i,0]=di

    difreq = difreq[difreq[:,1].argsort()][::-1]
    difreq = difreq[np.where(difreq[:,1]>freq)]

    print ("Digraphs:")
    print (difreq)
    print ("\n\n")
