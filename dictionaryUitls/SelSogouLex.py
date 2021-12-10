import sys
import os
sys.path.append('..')
from IOUtils.FileHelper import FileHelper

def coreDictLoader():
	wordlist = []
	path = 'E:/BaiduNetdiskDownload/core.ini'
	file = open(path,'r',encoding='utf-8')
	for line in file.readlines():
		items = line.strip().split('\t')
		wordlist.append(items[1])
	return wordlist

def selectWords():
	wordlist= coreDictLoader()
	sourcePath = 'E:\\迅雷下载\\sogoulex'
	dirlist = FileHelper.get_all_directories(sourcePath)

	for dirname in dirlist:
		filelist = FileHelper.get_all_files(dirname)
		for filename in filelist:
			words = []
			file = open(filename,'r',encoding='utf-8')
			for line in file.readlines():
				if line.strip() in wordlist:
					continue
				else:
					words.append(line.strip())
			if len(words) > 0:
				ndir = dirname.replace('迅雷下载','new')
				print(ndir)
				FileHelper.createDir(ndir)
				nfile = open(filename.replace('迅雷下载','new'),'w',encoding='utf-8')
				for word in words:
					nfile.write(word+'\n')
				nfile.close()



selectWords()
