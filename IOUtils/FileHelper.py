import os


def getFileAbsroutePathList(path):
    files = os.listdir(path)
    allfiles = []
    for file in files:
        allfiles.append(path + '\\' + file)
    return allfiles

def get_all_files(dir):
    files_ = []
    list_ = os.listdir(dir)
    for i in range(0, len(list_)):
        path = os.path.join(dir, list_[i])
        if os.path.isdir(path):
            files_.extend(get_all_files(path))
        if os.path.isfile(path):
            files_.append(path)
    return files_
