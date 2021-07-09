class CoreDictUtils():



    def getCoreInit(self):
        dict_init ={}
        path_init = 'E:/BaiduNetdiskDownload/2/core.ini'
        reader = open(path_init, mode='r', encoding="utf-8")
        for line in reader.readlines():
            items = line.strip().split('\t')
            k = items[1]
            if k in dict_init.keys():
                natures = dict_init[k]
                natures.append(items[0])
                dict_init[k] = natures
            else:
                natures = [items[0]]
                dict_init[k] = natures

        reader.close()
        return  dict_init

    #已迁移至分词系统
    def dictCompare(self):
        path_init = 'E:/BaiduNetdiskDownload/2/core.ini'
        path_corpus_dic = 'E:/BaiduNetdiskDownload/2/coreDic.txt'
        outpath = 'E:/BaiduNetdiskDownload/2/coreDic4Sys.txt'

        # dic_init = {}
        dic_new = {}
        natureset = []

        reader = open(path_corpus_dic, mode='r', encoding="utf-8")
        writer = open(outpath, mode='w', encoding="utf-8")

        for line in reader.readlines():
            items = line.strip().split('\t')
            nature = items[1];
            word = items[0]
            writer.write(line)
            key = word + '\t' + nature
            if len(items) < 3 :
                print(line)
            if key not in dic_new.keys():
                dic_new[key] = items[2]
        reader.close()

        reader = open(path_init, mode='r', encoding="utf-8")

        for sline in reader.readlines():
            items_init = sline.strip().split('\t')

            if items_init[0] == 'jsnr':
                continue
            if items_init[0] not in natureset:
                natureset.append(items_init[0])
            key_init = items_init[1] + '\t' + items_init[0]
            if key_init not in dic_new.keys():#不在语料词典中的词词频记为0
                # print(line)
                # writer.write(sline)
                writer.write(key_init +'\t' + str(0) + '\n')

        reader.close()
        writer.close()
        print(len(natureset))
        print(natureset)
        print('ok')


if __name__ == '__main__':
    cd = CoreDictUtils()
    cd.dictCompare()
