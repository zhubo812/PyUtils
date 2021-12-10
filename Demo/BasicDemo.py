

chardic = {}#字符词典 /字符频次记录器
first_char_dic={}

# 获取指定文本所有行
def getFileLines(path):#定义一个方法
    lines = []
    reader = open(path,mode='r',encoding='utf-8')#打开一个文本
    lines = reader.readlines()#读取文本所有行到一个列表
    return lines


def counter(dic, char):
    if char in dic:#判断字符char是否在字典dic中
        freq = dic[char]
        freq = freq +1
        dic[char]= freq
    else:
        dic[char]= 1



path = 'E:/BaiduNetdiskDownload/2/Japanese_Names_Corpus（18W）.txt'

lines = getFileLines(path)

for line in lines:#循环每一行
    sline = line.strip()
    if len(sline)==0:
        continue
    for c in sline:#循环一行文本中所有字符
        counter(chardic, c)
    firstchar = sline[0:1]
    counter(first_char_dic,firstchar)

    break
print(chardic)
print(first_char_dic)


print(len(chardic))
print(len(first_char_dic))