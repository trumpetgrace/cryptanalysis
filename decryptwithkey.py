from cryptoIO import TextToIntArray
from cryptoIO import IntArrayToText
import numpy as np

key = "RWQMHGCDNLUYBPKXESJZIVOAFT"

ciphertext = "ZDHCSRJXZDKICDCHPZYHRJROKBRPJ"


def decrypt(key, ciphertext):
    alphabet ="abcdefghijklmnopqrstuvwxyz"
    numalpha = TextToIntArray(alphabet)

    key = key.lower()
    numkey = TextToIntArray(key)

    ciphertext = ciphertext.lower()
    numcipher = TextToIntArray(ciphertext)

    x = np.zeros((len(ciphertext)), dtype="int")
    i = 0
    for num in numcipher:
        j = 0
        for n in x:
            if num == numkey[j]:
                x[i] = numalpha[j]
            else:
                j += 1
        i += 1

    plaintext = IntArrayToText(x)

    print ("Original:")
    print (ciphertext)
    print ("\n")
    print ("Decrypted:")
    print (plaintext)

decrypt(key, ciphertext)
