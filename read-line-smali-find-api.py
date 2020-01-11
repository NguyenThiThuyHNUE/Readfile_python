import os


def readFileSmali(inFile, outFile):
    f = open(inFile, "r")
    for x in f:
        if x.find('    invoke') != -1 or x.find('.method') != -1 or x.find('.end method') != -1 :
            # or x.find('.method') != -1 or x.find('.end method') != -1
            # print(x)
            outFile.write(x)


pass
inFile = "smali.txt"
resultFile = open("api-method-endMethod.txt", "w")

readFileSmali(inFile, resultFile)

resultFile.close()

# print('done!')
