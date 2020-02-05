import os
import re
import sys
import numpy as np
def matric_invoke(inFile, outFile):
    f = open(inFile, "r")
    count = sum(1 for line in open('api.txt'))
    countdemo = 0
    arr = []
    for line in f:
        arr.append(line)
    # print(arr)
    A = np.eye(count)
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][0:12] == arr[y][0:12]:
                A[x][y] = A[y][x] =1
    # print(A)
    outFile.write(str(A))
    #     i+=1
    #     for line1 in f:
    #         j+=1
    #         if line[0:15] == line1[0:15]:
    #             countdemo += 1
    #             print(line + line1)
    #         print(i,j)
    # print(countdemo)
    # outFile.write(str(A))

pass
inFile = "api.txt"
resultFile = open("matric-invoke.txt", "w")

matric_invoke(inFile, resultFile)

resultFile.close()

print('done!')

print()