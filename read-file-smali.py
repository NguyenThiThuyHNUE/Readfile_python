import os
def readAllFile(currentPath, outFile):
    fileList = os.listdir(currentPath)
    for name in fileList:
        fileName = currentPath + "/" + name
        if (os.path.isfile(fileName)):
            if ".smali" in fileName:
                f = open(fileName, "r")
                fileContent = f.readlines()
                outFile.write("\n------>" + fileName+": \n")
                #thisset = set()
                #for x in fileContent:
                 #   if '    invoke' in x:
                  #      thisset.add(x)
                        # outFile.write(x)
                #outFile.write(str(thisset))
                    #     print(x)
                # print(thisset)
                # for letter in thisset:
                #     outFile.write(letter)
                    # print(letter)
                        # outFile.write(x)
                        # print(x)
                # print(fileContent)
        else:
            if (os.path.isdir(fileName)):
                readAllFile(fileName, outFile)
pass

resultFile = open("smali.txt", "w")

readAllFile("/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/Stick/smali", resultFile)

resultFile.close()

print('done!')

# import os
#
# def readAllFile(currentPath, outFile):
#     fileList = os.listdir(currentPath)
#     for name in fileList:
#         fileName = currentPath + "/" + name
#         if (os.path.isfile(fileName)):
#             if ".smali" in fileName:
#                 f = open(fileName, "r")
#                 fileContent = f.read()
#                 outFile.write("\n------>" + fileName+": \n")
#                 outFile.write(fileContent)
#         else:
#             if (os.path.isdir(fileName)):
#                 readAllFile(fileName,outFile)
# pass
#
#
# resultFile = open("smali.txt", "w")
#
# readAllFile("/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/Stick/smali",resultFile)
#
# resultFile.close()
#
# print('done!')
