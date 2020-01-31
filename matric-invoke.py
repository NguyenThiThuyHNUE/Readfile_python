import os
import re
import sys

import os
import numpy as np

def matric_invoke(inFile, outFile):
    f = open(inFile, "r")
    non_blank_count = 0
    for line in f:
        if line.strip():
            non_blank_count += 1
    print(non_blank_count)
    np.eye(non_blank_count, k=non_blank_count)

pass
inFile = "api.txt"
resultFile = open("matric-invoke.txt", "w")

matric_invoke(inFile, resultFile)

resultFile.close()

print('done!')