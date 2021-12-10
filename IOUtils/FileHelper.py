import os

class FileHelper:
    def getFileAbsroutePathList(path):
        files = os.listdir(path)
        allfiles = []
        for file in files:
            allfiles.append(path + '\\' + file)
        return allfiles

    '''
    获取文件夹下所有文件
    '''
    def get_all_files(dir):
        fileslist = []
        for root, dirs, files in os.walk(dir, topdown=False):
            for name in files:
                fileslist.append(os.path.join(root, name))
        return fileslist

    def get_all_directories(dir):
        dirlist = []
        for root, dirs, files in os.walk(dir, topdown=False):
            for name in dirs:
                dirlist.append(os.path.join(root, name))
        return dirlist

    def createDir(filePath):
        if os.path.exists(filePath):
            print(filePath)
            return
        else:
            try:
                os.mkdir(filePath)
            except Exception as e:
                os.makedirs(filePath)
               