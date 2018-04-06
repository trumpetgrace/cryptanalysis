from cryptoIO import TextToIntArray
from cryptoIO import IntArrayToText
import numpy as np
import matplotlib.pyplot as plt

text = "LGUWUVGNUQMBOVCUMBWCJJOJMNNMSUPMWBAPCSAMDKVCBBOWSE\
VMSDKCSOADSNWRMBCUWDSWSUPMFDBJRBMIJWMRRCBAOUDUPWNNIMMAPLWSEJMOVCR\
MSDCSNFMBLGUPWNNWNUMBNECQMWUUPMWBPMCBUOCNNMSUCSRWSRGJEMRUPMWBVWBU\
PKDBNDVMUWVMCUUPMMYIMSNMDKUPMWBRMCBKBWMSRNQGJECBBMJCUWDSNFWUPCBMS\
MFCJDKUMSRMBSMNNPDFMQMBUPMOBMICWBMRUDPMBBDDVDSJMCQWSEUPMRWSWSEICB\
JDGBCSRNCUFWUPPMBUWJJNGVVDSMRUDADKKMMNPMFCNNUWJJQMBOIDDBJOCSRMJWH\
CLMUPFDGJRSDUXGWUPMBCUCJJ"

def getFrequency(ciphertext):

    alphabet ="abcdefghijklmnopqrstuvwxyz"
    numalpha = TextToIntArray(alphabet)

    ciphertext = ciphertext.lower()
    numcipher = TextToIntArray(ciphertext)

    letterFreq = np.zeros(26, dtype=int)
    relFreq = np.zeros(26, dtype=float)
    totalFreq = len(ciphertext)

    # shifts alphabet from 0-25 to 1-26
    for num in numcipher:
        letterFreq[num] = letterFreq[num] + 1

    # get relative frequencies
    i = 0
    for num in letterFreq:
        relFreq[i] = letterFreq[i] / totalFreq * 100
        i += 1

    cipheralpha =[]

    i = 0
    for num in relFreq:
        cipheralpha.append(i)
        i += 1

    cipheralpha = IntArrayToText(cipheralpha)

    print ("Letter frequency:")

    i = 0
    for num in relFreq:
        print (cipheralpha[i], ",", relFreq[i])
        i += 1

    print ("\n\n")
    print ("Total number of letters:")
    print (totalFreq)
    print ("\n\n")

    cipherFreq = [x for _,x in sorted(zip(relFreq, cipheralpha), reverse=True)]

    generalFreq = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "d", "l", "u", "c", "m", "f", "y", "w", "g", "p", \
    "b", "v", "k", "x", "q", "j", "z"]
    key = [x for _,x in sorted(zip(generalFreq, cipherFreq))]
    numkey = TextToIntArray(key)

    print ("Cipher Letter Frequency:")
    print (cipherFreq)
    print ("General Letter Frequency:")
    print (generalFreq)
    print ("Key:")
    print (key)
    subInKey(ciphertext, numcipher, numkey, numalpha)
    # displayFrequency(numalpha, relFreq)
    asking = True
    while asking:
        print ("\n\n")
        makeChange = input("Would you like to swap letters? ")
        makeChange.lower()
        if makeChange == "yes":
            cipherFreq, generalFreq, key, numkey = validLetters(cipherFreq, generalFreq, key)

            subInKey(ciphertext, numcipher, numkey, numalpha)
        elif makeChange == "no":
            asking = False
        else:
            print ("Invalid input, please choose yes or no")

def validLetters(cipherFreq, generalFreq, key):
    print ("\n")
    print ("Pick two letters from the general Frequency array to swap (in the format: ab)")
    asking = True
    while asking:
        letters = input("Letters to swap: ")
        if len(letters) == 2:
            usedChars = []
            for c in letters:
                if c in usedChars:
                    print ("Invalid input, please choose two different letters")
                    asking = True
                elif c == " ":
                    print ("Invalid input, please enter two letters")
                    asking = True
                else:
                    usedChars.append(c)
                    asking = False
        elif len(letters) != 2:
            print ("Please enter two letters (in the format: ab)")
    return swapLetters(cipherFreq, generalFreq, key, letters)
    # print (numkey)

def swapLetters(cipherFreq, generalFreq, key, letters):
    first = letters[0]
    second = letters[1]
    pos1, pos2 = generalFreq.index(first), generalFreq.index(second)
    generalFreq[pos1], generalFreq[pos2] = generalFreq[pos2], generalFreq[pos1]
    print ("\n\n")
    print ("Cipher Letter Frequency:")
    print (cipherFreq)
    print ("General Letter Frequency")
    print (generalFreq)
    key = [x for _,x in sorted(zip(generalFreq, cipherFreq))]
    global numkey
    numkey = TextToIntArray(key)
    print ("Key:")
    print (key)

    return cipherFreq, generalFreq, key, numkey

def subInKey(ciphertext, numcipher, numkey, numalpha):

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

    print ("\n\n")
    print ("Original:")
    print (ciphertext)
    print ("\n\n")
    print ("Deciphered:")
    print (plaintext)
    print ("=========================")

def displayFrequency(numalpha, relFreq):

    x = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',\
    'T','U','V','W','X','Y','Z']

    barfreq = plt.axes()
    barfreq.bar(numalpha, relFreq, width=0.4)
    barfreq.set_xticks(np.arange(len(x)))
    barfreq.set_xticklabels(x)
    barfreq.set_ylabel("Frequency")
    barfreq.set_title("Letter Frequencies in Ciphertext")
    plt.show()
