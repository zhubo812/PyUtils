# coding=utf-8
import os
import sys
import requests

from urllib.request import urlretrieve
from bs4 import BeautifulSoup


class SouGSpider(object):
    def __init__(self):
        self.base_url = "http://pinyin.sogou.com"
        self.homepage_url = "http://pinyin.sogou.com/dict/"
        self.base_dir = "HMM/lexlib"

    def callbackfunc(self, blocknum, blocksize, totalsize):
        """
        回调函数
        :param blocknum: 已经下载的数据块
        :param blocksize:  数据块的大小
        :param totalsize: 远程文件的大小
        :return:
        """
        percent = 100.0 * blocknum * blocksize / totalsize
        if percent > 100:
            percent = 100
        sys.stdout.write("\r%6.2f%%" % percent)
        sys.stdout.flush()

    def load(self):
        html = requests.get(self.homepage_url).text
        soup = BeautifulSoup(html, "html.parser")
        soup = soup.find(id="dict_category_show").find_all('div', class_='dict_category_list')
        fc = 0
        sc = 0
        tc = 0
        for ii in soup:
            fc += 1
            print("Level 1 :" + ii.find(class_='dict_category_list_title').find('a').contents[0])#Level 1 获取指定领域页面链接
            first_dir = os.path.join(self.base_dir, ii.find(class_='dict_category_list_title').find('a').contents[0])#拼接存储词表路径
            os.makedirs(first_dir, exist_ok=True)

            #获取Level 2 词表集链接
            for k in ii.find(class_='catewords').find_all('a'):
                secondclass = k.contents[0]
                second_url = self.base_url + "%s" % (k['href'])
                print(" " * 4 + "Level 2 :" + secondclass)
                print(second_url)
                second_dir = os.path.join(first_dir, secondclass)
                os.makedirs(second_dir, exist_ok=True)#创建Level 2 词表路径

                sc += 1
                soup2 = BeautifulSoup(requests.get(second_url).text, "html.parser")
                totalpagenum = soup2.find(id='dict_page_list').find('ul').find_all('span')[-2].a.contents[0]

                os.chdir(second_dir)
                for pageind in range(1, int(totalpagenum) + 1):
                    soup2 = BeautifulSoup(requests.get("%s/default/%d" % (second_url.replace("?rf=dictindex", ""), pageind)).text, "html.parser")
                    for kk in soup2.find_all('div', class_='dict_detail_block'):
                        thirdclass = kk.find(class_='detail_title').find('a').contents[0]
                        third_url = kk.find(class_='dict_dl_btn').a['href']
                        print(" " * 8 + "Level 3 :" + thirdclass + " " * 10 + "Downloading")
                        tc += 1
                        try:
                            urlretrieve(third_url, "{}.scel".format(thirdclass), self.callbackfunc)#下载词表
                        except Exception as e:
                            print(e)
                            print(secondclass)
                            print(thirdclass)

        print("Total :%d, %d, %d" % (fc, sc, tc))


if __name__ == "__main__":

    sg = SouGSpider()
    sg.load()
