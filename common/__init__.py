import os


def down(fileDir, fileName, content):
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
    if os.path.exists(fileName):
        print(fileName + "已存在")
        return
    file = open(fileName, 'wb')
    file.write(content)
    file.close()
