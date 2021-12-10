#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import IOUtils.FileHelper
import NLPUtils.StringUtils


class RMRBUtils:

    def strQ2B(self, ustring):
        """全角转半角"""
        rstring = ""
        for uchar in ustring:
            inside_code = ord(uchar)
            if inside_code == 12288:  # 全角空格直接转换
                inside_code = 32
            elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
                inside_code -= 65248

            rstring += chr(inside_code)
        return rstring

    def getBigWord(self, line, pattern):
        sline = line.strip()
        res = pattern.findall(sline)
        for token in res:
            words = token.split('  ')
            newword = ''
            for w in words:
                items = w.split('/')
                newword = newword + items[0]
            sline = sline.replace('[' + token + ']', newword + '/')
        return sline

    def getDocName(self, line, pattern):
        sline = line.strip()
        res = pattern.findall(sline)
        for token in res:
            words = token.split('  ')
            newword = ''
            for w in words:
                items = w.split('/')
                newword = newword + items[0]
            sline = sline.replace(token, newword + '/nz')
        return sline

    def getBigWordLine(self, line):
        sline = line.replace('/%', '')
        # print(sline)
        result = ''
        # 合并语料中的机构名
        pattern = re.compile('\[(.+?)\]')
        sline = RMRBUtils().getBigWord(sline, pattern)

        # 合并语料中的书名、文件名
        pattern = re.compile('《.+?》/w')
        sline = RMRBUtils().getDocName(sline, pattern)

        words = sline.split('  ')
        wordlist = []
        idx = -1
        if len(words) > 1:
            for i in range(0, len(words) - 1):
                if idx == i:
                    continue

                word1 = NLPUtils.StringUtils.getNature(words[i])
                word2 = NLPUtils.StringUtils.getNature(words[i + 1])
                nature1 = NLPUtils.StringUtils.getNature(words[i])
                nature2 = NLPUtils.StringUtils.getNature(words[i + 1])

                if nature1 == 'nr' and nature2 == 'nr':
                    nw = word1 + word2 + '/nr'
                    wordlist.append(nw)
                    idx = i + 1
                    if idx == len(words) - 2:
                        wordlist.append(words[idx + 1])
                elif nature1 == 't' and nature2 == 't':
                    nw = word1 + word2 + '/t'
                    wordlist.append(nw)
                    idx = i + 1
                    if idx == len(words) - 2:
                        wordlist.append(words[idx + 1])
                else:
                    wordlist.append(words[i])
                    if i == len(words) - 2:
                        wordlist.append(words[i + 1])
        else:
            wordlist = words
        words = wordlist
        wordlist = []
        idx = -1
        if len(words) > 1:
            for i in range(0, len(words) - 1):
                if idx == i:
                    continue
                word1 = NLPUtils.StringUtils.getNature(words[i])
                word2 = NLPUtils.StringUtils.getNature(words[i + 1])
                nature1 = NLPUtils.StringUtils.getNature(words[i])
                nature2 = NLPUtils.StringUtils.getNature(words[i + 1])
                if nature1 == 't' and nature2 == 't':
                    nw = word1 + word2 + '/t'
                    wordlist.append(nw)
                    idx = i + 1
                    if idx == len(words) - 2:
                        wordlist.append(words[idx + 1])
                else:
                    wordlist.append(words[i])
                    if i == len(words) - 2:
                        wordlist.append(words[i + 1])
        else:
            wordlist = words
        for word in wordlist:
            result = result + ' ' + word

        return result.strip()

    def getNaturesCounter(self):
        dic = {}
        path = "E:/BaiduNetdiskDownload/2/RenminRibao1998_BigWord.txt"
        print(path)
        reader = open(path, mode='r', encoding="utf-8")
        # writer = open("E:/BaiduNetdiskDownload/rm.txt",mode='w',encoding='utf-8')

        lines = reader.readlines()
        for line in lines:
            sline = line.strip()
            # print(sline)
            if (len(sline.strip()) == 0):
                continue
            items = sline.split('\t')
            if (len(items) < 2):
                print(sline)
                continue
            sline = items[1].strip()
            words = sline.split(' ')
            for word in words:
                if (len(word.strip()) == 0):
                    continue
                nature = word[word.rfind('/') + 1:]

                if nature not in dic.keys():
                    dic[nature] = 1
                else:
                    freq = dic[nature]
                    dic[nature] = freq + 1
        # break
        return dic
    #已整合入分词系统
    def natureReplacer(self):
        path = "E:/BaiduNetdiskDownload/2/RenminRibao1998_BigWord.txt"
        outpath = "E:/BaiduNetdiskDownload/2/RenminRibao1998_BigWord_NatureTrans.txt"
        writer = open(outpath, mode='w', encoding='utf-8')
        print(path)
        reader = open(path, mode='r', encoding="utf-8")
        lines = reader.readlines()
        for line in lines:
            wordlist = []
            sline = line.strip()
            if (len(sline.strip()) == 0):
                continue
            items = sline.split('\t')
            if (len(items) < 2):
                print(sline)
                continue
            sline = items[1].strip()
            tokens = sline.split(' ')
            for token in tokens:
                word = NLPUtils.StringUtils.getWord(token)
                nature = NLPUtils.StringUtils.getNature(token).lower()
                if nature == 'vn':
                    nature = 'n'
                elif nature == 'an':
                    nature = 'n'
                elif nature == 'vd' or nature == 'ad':
                    nature = 'd'
                # elif word=='的' and nature=='ng':
                #     print(line)
                ntoken = word + '/' + nature
                wordlist.append(ntoken)

            sline = ' '.join(wordlist)
            writer.write(items[0] + '\t' + sline + '\n')
        writer.close()

    def getWordNaturesCounter(self):
        dic = {}
        naturelist = ['nr', 't', 'm', 'nz']
        path = "E:/BaiduNetdiskDownload/2/RenminRibao1998_BigWord_NatureTrans.txt"
        outpth = 'E:/BaiduNetdiskDownload/2/rmrbworddic.txt'
        print(path)
        reader = open(path, mode='r', encoding="utf-8")
        writer = open(outpth, mode='w', encoding='utf-8')

        lines = reader.readlines()
        for line in lines:
            sline = line.strip()
            # print(sline)
            if (len(sline.strip()) == 0):
                continue
            items = sline.split('\t')
            if (len(items) < 2):
                print(sline)
                continue
            sline = items[1].strip()
            tokens = sline.split(' ')
            for token in tokens:
                if (len(token.strip()) == 0):
                    continue
                word = NLPUtils.StringUtils.getWord(token)
                nature = NLPUtils.StringUtils.getNature(token)

                ntoken = word + '\t' + nature

                if ntoken not in dic.keys():
                    dic[ntoken] = 1
                else:
                    freq = dic[ntoken]
                    dic[ntoken] = freq + 1
        # break
        for k, v in dic.items():
            sline = k + '\t' + str(v) + '\n'
            writer.write(sline)

        writer.close()
        reader.close()

    def getSignleWordNaturesCounter(self):
        dic = {}
        naturelist = ['nr', 't', 'm', 'nz']
        path = "E:/BaiduNetdiskDownload/2/RenminRibao1998_BigWord_NatureTrans.txt"
        outpth = 'E:/BaiduNetdiskDownload/2/rmrbworSingleWordddic.txt'
        print(path)
        reader = open(path, mode='r', encoding="utf-8")
        writer = open(outpth, mode='w', encoding='utf-8')

        lines = reader.readlines()
        for line in lines:
            sline = line.strip()
            # print(sline)
            if (len(sline.strip()) == 0):
                continue
            items = sline.split('\t')
            if (len(items) < 2):
                print(sline)
                continue
            sline = items[1].strip()
            tokens = sline.split(' ')
            for token in tokens:
                if (len(token.strip()) == 0):
                    continue

                word = NLPUtils.StringUtils.getWord(token)
                nature = NLPUtils.StringUtils.getNature(token)

                if word not in dic.keys():
                    wlist = []
                    wlist.append(nature)
                    dic[word] = wlist
                else:
                    wlist = dic[word]
                    if nature not in wlist:
                        wlist.append(nature)
                        dic[word] = wlist
        # break
        for k, v in dic.items():
            counter = len(v)
            if(counter==1):
                continue
            sline = k + '\t' + str(counter) + '\t' + ' '.join(v) + '\n'
            writer.write(sline)

        writer.close()
        reader.close()

    #已整合入分词系统
    def data2Dictionary(self):
        natureset = {}
        coredic = {}
        path = "E:/BaiduNetdiskDownload/2/RenminRibao1998_BigWord_NatureTrans.txt"
        outpth = 'E:/BaiduNetdiskDownload/2/coreDic.txt'
        outpth_longword = 'E:/BaiduNetdiskDownload/2/longword.txt'
        print(path)
        reader = open(path, mode='r', encoding="utf-8")
        writer = open(outpth, mode='w', encoding='utf-8')
        writer_longword = open(outpth_longword, mode='w', encoding='utf-8')

        lines = reader.readlines()
        for line in lines:
            sline = line.strip()
            # print(sline)
            if (len(sline.strip()) == 0):
                continue
            items = sline.split('\t')
            if (len(items) < 2):
                print(sline)
                continue
            sline = items[1].strip()
            tokens = sline.split(' ')
            for token in tokens:
                if (len(token.strip()) == 0):
                    continue

                word = NLPUtils.StringUtils.getWord(token)
                nature = NLPUtils.StringUtils.getNature(token)
                if len(word.strip()) == 0:
                    continue

                key = word + '\t' + nature

                if key not in coredic.keys():
                    coredic[key] = 1
                else:
                    freq = coredic[key]
                    freq += 1
                    coredic[key] = freq

                if nature not in natureset.keys():
                    natureset[nature]=1
                else:
                    freq= natureset[nature]
                    freq += 1
                    natureset[nature] = freq
        # break
        print(' '.join(list(natureset.keys())))
        # for k in natureset.keys():
        #     print(k)
        stoplist =['nz','nt','m','nr','nx']
        for k, v in coredic.items():
            els = k.split('\t')
            wordlen = len(els[0])
            if(els[1] in stoplist):
                continue
            elif(els[1] == 't'):
                if v <3:
                    continue
                else:
                    if('年' in els[0] or '月' in els[0] or '日' in els[0] or '时' in els[0]):
                        continue
            elif (wordlen > 6 and els[1] != 'l' and els[1] != 'i'):
                writer_longword.write(k + '\t' + str(v) + '\t' + str(wordlen) + '\n')
                continue
            elif( '(' in els[0] and wordlen > 1 ):
                writer_longword.write(k + '\t' + str(v) + '\t' + str(wordlen) + '\n')
                continue
            # sline = k + '\t' + str(v) + '\t' + str(wordlen) + '\n'
            sline = els[0] + '\t' +els[1]+ '\t' + str(v) +  '\n'
            writer.write(sline)


        writer.close()
        reader.close()




if __name__ == '__main__':
    # line = '车耳/nr'
    # word = NLPUtils.StringUtils.getWord(line)
    # nature = NLPUtils.StringUtils.getNature(line)
    # print(word)
    # print(nature)
    # ============

    # RMRBUtils().getWordNaturesCounter()
    # 创建词性转移矩阵数据
    # ==========================
    # RMRBUtils().natureReplacer()#转换词性标记
    RMRBUtils().getSignleWordNaturesCounter()#生成单词及其词性对应关系
    # RMRBUtils().data2Dictionary()#生成基础词汇词典
