import os
thisset = set()
def readAllFile(currentPath, outFile):
    fileList = os.listdir(currentPath)
    for name in fileList:
        fileName = currentPath + "/" + name
        if (os.path.isfile(fileName)):
            if ".smali" in fileName:
                f = open(fileName, "r")
                fileContent = f.readlines()
                # outFile.write("\n------>" + fileName+": \n")
                for x in fileContent:
                   if "    invoke" in x:
                       if x not in thisset:
                        thisset.add(x[x.find("L"):x.find("(")] + "\n")
                        # thisset.add(x[x.find("->"):x.find("(")] + "\n")
        else:
            if (os.path.isdir(fileName)):
                readAllFile(fileName, outFile)
pass
resultFile = open("API-package.txt", "w")
automatic = open("../Automatic reverse translation/Automatic-reverse-translation.txt", "r")
path = ""
for line in automatic:
    path ="/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/malware_samples/"+line.strip()+"/smali"
    readAllFile(path, resultFile)
for letter in thisset:
    resultFile.write(letter)
resultFile.close()
print('done!')