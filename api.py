import os
import numpy as np

def readFileSmali(inFile, outFile):
    f = open(inFile, "r")
    thisset = {""}
    for x in f:
        thisset.add(x)
        # outFile.write(str(thisset))
    # outFile.write(str(len(thisset)))
    for letter in set(thisset):
            outFile.write(letter)
    # outFile.write(str(len(thisset)))
pass
inFile = "list-api-coincide.txt"
resultFile = open("api.txt", "w")

readFileSmali(inFile, resultFile)

resultFile.close()

print('done!')

# thisset = {"apple", "banana", "cherry","apple"}
#
# # thisset.add("apple")
#
# print(set(thisset))