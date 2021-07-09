#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import copy
import NLPUtils.StringUtils


class WordNatureMatrix:

    def cal_hmm_matrix(self):
        # 得到所有标签
        tags_num={}
        tags_list = ["begin", "v", "n", "u", "a", "w", "t", "m", "q", "nt",
                     "nr", "nz", "vg", "k", "p", "f", "r", "c", "ns",
                     "s", "d", "j", "l", "b", "i", "ng", "z", "tg",
                     "y", "nx", "ag", "o", "dg", "h", "rg", "e", "mg", "yg", "end"]
        for nature in tags_list:
            if nature not in tags_num:
                tags_num[nature]=0

        # 转移矩阵、发射矩阵
        transaction_matrix = np.zeros((len(tags_list), len(tags_list)), dtype=float)
        # emission_matrix = np.zeros((len(tags_list), len(observation)), dtype=float)

        # 计算转移矩阵和发射矩阵
        word_file = open('E:/BaiduNetdiskDownload/2/RenminRibao1998_BigWord_NatureTrans.txt',
                         encoding='utf-8').readlines()
        for line in word_file:
            if line.strip() != '':
                word_pos_list = line.strip().split('\t')[1].split(' ')
                word_pos_list.insert(0, 's/begin')
                word_pos_list.append('s/end')
                for i in range(1, len(word_pos_list)):
                    tag = NLPUtils.StringUtils.getNature(word_pos_list[i])
                    pre_tag = NLPUtils.StringUtils.getNature(word_pos_list[i - 1])

                    transaction_matrix[tags_list.index(pre_tag)][tags_list.index(tag)] += 1
                    tags_num[tag] += 1
        outpath_matrix = 'E:/BaiduNetdiskDownload/2/matrix.txt'
        outpath_init = 'E:/BaiduNetdiskDownload/2/init.txt'
        writer = open(outpath_matrix, mode='w', encoding='utf-8')
        writer_init = open(outpath_init, mode='w', encoding='utf-8')


        # 转移矩阵平滑
        for row in range(transaction_matrix.shape[0]):
            n = np.sum(transaction_matrix[row])
            transaction_matrix[row] += 1e-16
            transaction_matrix[row] /= n + 1

        for row in transaction_matrix:
            sline = '\t'.join(str(x) for x in row)
            # print(sline)
            writer.write(sline+'\n')
        writer.close()
        # 发射矩阵平滑

        # 将储存词性频次的字典更新为储存词性频率,也就是初始概率
        times_sum = sum(tags_num.values())
        init_tags = copy.deepcopy(tags_num)
        for item in tags_num.keys():
            tags_num[item] = tags_num[item] / times_sum

        for k , v in tags_num.items():
            sline = k+'\t'+ str(v)+'\t'+  str(init_tags[k])+'\n'
            writer_init.write(sline)
        writer_init.close()
        # 返回隐状态，初始概率，转移概率，发射矩阵概率
        return tags_list, list(tags_num.values()), transaction_matrix

if __name__ == '__main__':
    WordNatureMatrix().cal_hmm_matrix()
    # transaction_matrix = np.zeros((5, 5), dtype=float)
    #
    # print(transaction_matrix)
    # for row in transaction_matrix:
    #     sline = ' '.join(str(x) for x in row)
    #     print(sline)
    # dic1 ={"1":1,"2":2}
    # dic2 = copy.deepcopy(dic1)
    # dic1["1"]=3
    # print(dic2)