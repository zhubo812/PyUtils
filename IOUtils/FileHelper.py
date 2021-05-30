import os


def getFileAbsroutePathList(path):
    files = os.listdir(path)
    allfiles = []
    for file in files:
        allfiles.append(path + '\\' + file)
    return allfiles