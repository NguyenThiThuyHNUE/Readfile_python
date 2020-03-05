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
                for x in fileContent:
                   if '    invoke' in x:
                       if x not in thisset:
                        thisset.add( fileName[fileName.find('c/'):fileName.find('/smali')] + x)
        else:
            if (os.path.isdir(fileName)):
                readAllFile(fileName, outFile)
pass
resultFile = open("read-line-smali-app.txt", "w")
automatic = open("../Automatic reverse translation/Automatic-reverse-translation.txt", "r")
path = ""
for line in automatic:
    path ="/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/"+line.strip()+"/smali"
    readAllFile(path, resultFile)
for letter in thisset:
    resultFile.write(letter)
resultFile.close()
print('done!')
