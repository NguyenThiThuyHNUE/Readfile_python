import os
import re
import sys


def readFileSmali(inFile, outFile):
    f = open(inFile, "r")
    count = 0
    for x in f:
        count +=1
        # if not x.strip(): continue
        if x.find('invoke') != -1 or x.find('.method') != -1 or x.find('.end method') != -1:
        # or x.find('.method') != -1 or x.find('.end method') != -1
        # print(x)
            outFile.write(x)
        #     print(x)
        #     break

    # print(count)



pass
inFile = "smali.txt"
resultFile = open("api-method-endMethod.txt", "w")

readFileSmali(inFile, resultFile)

resultFile.close()

print('done!')
