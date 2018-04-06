from cryptoIO import TextToIntArray
from cryptoIO import IntArrayToText
import numpy as np
import matplotlib.pyplot as plt

def getTrigraphs(ciphertext):
    ciphertext = ciphertext.lower()

    if len(ciphertext) > 300:
        freq = int(len(ciphertext)/200)
    else:
        freq = 1

    # make lists length of alphabet
    array1 = np.arange(26)
    array2 = np.arange(26)
    array3 = np.arange(26)

    # n-dimensional array (array1xarray2)
    array1, array2, array3 = np.meshgrid(array1, array2, array3)

    # listifies array?
    array1 = array1.flatten()
    array2 = array2.flatten()
    array3 = array3.flatten()

    # converts numbers to letters

    array1 = IntArrayToText(list(array1))
    array2 = IntArrayToText(list(array2))
    array3 = IntArrayToText(list(array3))

    # turn into tuple
    tuples = np.array([(array1[i] + array2[i] + array3[i]) for i in range(17576)])
    # print (tuples)

    length = len(ciphertext)

    trigrapharray = np.array([ciphertext[i:i+3] for i in range(int(length-2))])
    # print(trigrapharray)

    trifreq = np.empty((17576,2), dtype="object")

    for i,tri in enumerate(tuples):
        trifreq[i,1]=(tri == trigrapharray).sum()
        trifreq[i,0]=tri

    trifreq = trifreq[trifreq[:,1].argsort()][::-1]
    trifreq = trifreq[np.where(trifreq[:,1]>freq)]

    print ("Trigraphs:")
    print (trifreq)
    print ("\n\n")
