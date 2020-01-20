import os
import numpy as np

def readFileSmali(inFile, outFile):
    global test_matrix
    count = 0
    f = open(inFile, "r")
    for x in f:
        if x.find('    invoke') != -1:
            outFile.write(x)
pass
inFile = "api-method-endMethod.txt"
resultFile = open("list-api-coincide.txt", "w")

readFileSmali(inFile, resultFile)

resultFile.close()

print('done!')