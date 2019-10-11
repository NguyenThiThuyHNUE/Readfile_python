import os

def readAllFile(currentPath, outFile):
    fileList = os.listdir(currentPath)
    for name in fileList:
        fileName = currentPath + "/" + name
        if (os.path.isfile(fileName)):
            if ".smali" in fileName:
                f = open(fileName, "r")
                fileContent = f.read()
                outFile.write("\n------>" + fileName+": \n")
                outFile.write(fileContent)
        else:
            if (os.path.isdir(fileName)):
                readAllFile(fileName,outFile)
pass


resultFile = open("tmp.txt","w")

readAllFile("/home/thuy/dich_nguoc/file_apk/com.royal.gamvip.v1.0.23/smali",resultFile)

resultFile.close()

print('done!')