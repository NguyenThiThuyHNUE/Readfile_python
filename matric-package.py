import os
import re
import sys
import numpy as np
def matric_package(inFile, outFile):
    f = open(inFile, "r")
    count = sum(1 for line in open('API-package.txt'))
    arr = []
    for line in f:
        arr.append(line)
    A = np.eye(count)
    print(A)
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][arr[x].find(', L'):arr[x].find(';')] == arr[y][arr[y].find(', L'):arr[y].find(';')]:
                A[x][y] = 1
    # print(A)
    # outFile.write(str(A))
pass
inFile = "api.txt"
resultFile = open("matric-package.txt", "w")

matric_package(inFile, resultFile)

resultFile.close()

print('done!')

print()