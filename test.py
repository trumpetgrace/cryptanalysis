from cryptoIO import TextToIntArray
from cryptoIO import IntArrayToText
import numpy as np
from frequencyanalysis import getFrequency, validLetters, swapLetters, subInKey
from digraph import getDigraphs
from trigraph import getTrigraphs

ciphertext = "LGUWUVGNUQMBOVCUMBWCJJOJMNNMSUPMWBAPCSAMDKVCBBOWSE\
VMSDKCSOADSNWRMBCUWDSWSUPMFDBJRBMIJWMRRCBAOUDUPWNNIMMAPLWSEJMOVCR\
MSDCSNFMBLGUPWNNWNUMBNECQMWUUPMWBPMCBUOCNNMSUCSRWSRGJEMRUPMWBVWBU\
PKDBNDVMUWVMCUUPMMYIMSNMDKUPMWBRMCBKBWMSRNQGJECBBMJCUWDSNFWUPCBMS\
MFCJDKUMSRMBSMNNPDFMQMBUPMOBMICWBMRUDPMBBDDVDSJMCQWSEUPMRWSWSEICB\
JDGBCSRNCUFWUPPMBUWJJNGVVDSMRUDADKKMMNPMFCNNUWJJQMBOIDDBJOCSRMJWH\
CLMUPFDGJRSDUXGWUPMBCUCJJ"

getDigraphs(ciphertext)
getTrigraphs(ciphertext)
getFrequency(ciphertext)

# this is the key:
# ['c', 'l', 'a', 'r', 'm', 'k', 'e', 'p', 'w', 'z', 't', 'j', 'v', 's', 'd', 'i', 'x', 'b', 'n', 'u', 'g', 'q', 'f', 'y', 'o', 'h']
# !!!!!!!!!!!!!!!!!
