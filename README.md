Cryptanalysis
=============

Text can be encrypted using encrypt.py.

Text can be decrypted using decrypt.py which will give the digraphs, trigraphs, and single letter frequency analysis
of a given ciphertext. This imports functions from three files, digraph.py, trigraph.py, and frequencyanalysis.py.
Letters can then be swapped and substituted in until the ciphertext is decrypted.

In frequencyanalysis.py there is also a graph function which can display the letter frequency in the given ciphertext.

Both of these files use cryptoIO which contains two useful commands: `TextToIntArray()` and `IntArrayToText()`
which substitutes numbers 0-25 for letters in a string and which substitutes letters for numbers 0-25, respectively.
