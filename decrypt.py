from cryptoIO import TextToIntArray
from cryptoIO import IntArrayToText
import numpy as np
from frequencyanalysis import getFrequency, validLetters, swapLetters, subInKey
from digraph import getDigraphs
from trigraph import getTrigraphs

def inputText():
    ciphertext = input("Input text to be decrypted: ")
    print ("\n\n")
    getDigraphs(ciphertext)
    getTrigraphs(ciphertext)
    getFrequency(ciphertext)

inputText()
