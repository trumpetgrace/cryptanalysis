from cryptoIO import TextToIntArray
from cryptoIO import IntArrayToText
import numpy as np

key = "CHXOWJETUINLFDYABRGKVPSQMZ"

def encrypt(key):

    plaintext = input("Plaintext (no spaces or punctuation): ")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numalpha = TextToIntArray(alphabet)

    key = key.lower()
    numkey = TextToIntArray(key)

    plaintext = plaintext.lower()
    numplaintext = TextToIntArray(plaintext)

    x = np.zeros((len(plaintext)), dtype="int")
    i = 0
    for num in numplaintext:
        x[i] = numkey[num]
        i += 1

    ciphertext = IntArrayToText(x)
    print ("Original:")
    print (plaintext)
    print ("\n")
    print ("Encrypted:")
    print (ciphertext)

encrypt(key)
