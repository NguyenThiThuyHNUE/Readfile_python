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
                    if x.find('.method') != -1 or x.find('    invoke') != -1:
                        if x not in thisset:
                            thisset.add(x)
                            # thisset.add(x[x.find("L"):x.find("(")] + "\n")
        else:
            if (os.path.isdir(fileName)):
                readAllFile(fileName, outFile)


pass
resultFile = open("read-line-smali-block.txt", "w")
automatic = open("Automatic-reverse-translation.txt", "r")
path = ""
for line in automatic:
    path = "/home/dieuthuy/Khoa-luan-tot-nghiep/dich-nguoc/" + line.strip() + "/smali"
    readAllFile(path, resultFile)
for letter in thisset:
    resultFile.write(letter)
resultFile.close()
read_file_block = open('read-line-smali-block.txt', 'r+')
count = sum(1 for line in open('read-line-smali-block.txt'))
arr = []
for line in read_file_block:
    arr.append(line)
# print(arr)
i = ''
api_block= open('API-block.txt', 'w')
for x in range(-1,len(arr)):
    if arr[x].find('.method') != -1:
        i = arr[x]
        continue
    # print(i.strip() +"0"+ arr[x])
    api_block.write(i.strip() + arr[x])
print('done!')
