import pymysql
import IOUtils.FileHelper
from Rmrb import RMRBUtils as rm
class MySQLHelper:
    def saveData2DB(self):
        # 打开数据库连接
        db = pymysql.connect(host="192.168.1.105",user="root",password="admin",database="corpus" )
        cursor = db.cursor()
        path = "E:/BaiduNetdiskDownload/r"
        print(path)
        files = IOUtils.FileHelper.getFileAbsroutePathList(path)

        for file in files:
            print(file)
            reader= open(file, mode='r',encoding="utf-8")
            # writer = open("E:/BaiduNetdiskDownload/rm.txt",mode='w',encoding='utf-8')
            try:
                # print(reader.read())
                    # line= reader.read()
                lines = reader.readlines()
                for line in lines:
                    # print(line)
                    sline = line.strip()
                    if(len(line.strip())==0):
                        continue
                    idstr = sline[0:19].replace('-','')
                    sline = sline[21:].strip()
                    sline = rm.strQ2B(self, sline)
                    sline = sline.replace('/%', '')
                    # print(sline)

                    print(len(idstr))
                    # writer.write(idstr+'\t'+sline+'\n')
                    # SQL 插入语句
                    sql = "INSERT INTO RenminRibao1998(tid,text)VALUES ('%s', '%s')"%(idstr,sline)
                    print(sql)
                    try:
                        # 执行sql语句
                        cursor.execute(sql)
                        # 提交到数据库执行
                        db.commit()
                    except Exception as e:
                        # 如果发生错误则回滚
                        db.rollback()
                        print(str(e))
            except UnicodeDecodeError:
                pass
        # writer.close()
        cursor.close()
        db.close()



    def saveBigWordData2DB(self):
        # 打开数据库连接
        db = pymysql.connect(host="192.168.1.105",user="root",password="admin",database="corpus" )
        cursor = db.cursor()
        path = "E:/BaiduNetdiskDownload/r"
        print(path)
        files = IOUtils.FileHelper.getFileAbsroutePathList(path)

        for file in files:
            print(file)
            reader= open(file, mode='r',encoding="utf-8")
            # writer = open("E:/BaiduNetdiskDownload/rm.txt",mode='w',encoding='utf-8')
            try:
                # print(reader.read())
                    # line= reader.read()
                lines = reader.readlines()
                for line in lines:
                    # print(line)
                    sline = line.strip()
                    if(len(line.strip())==0):
                        continue
                    idstr = sline[0:19].replace('-','')
                    sline = sline[21:].strip()
                    sline = rm.strQ2B(self,sline)
                    sline = rm.getBigWordLine(self,sline)
                    # print(sline)
                    print(len(idstr))
                    # writer.write(idstr+'\t'+sline+'\n')

                    # SQL 插入语句
                    sql = "INSERT INTO RenminRibao1998_BigWord(tid,text)VALUES ('%s', '%s')"%(idstr,sline)
                    print(sql)
                    try:
                        # 执行sql语句
                        cursor.execute(sql)
                        # 提交到数据库执行
                        db.commit()
                    except Exception as e:
                        # 如果发生错误则回滚
                        db.rollback()
                        print(str(e))
            except UnicodeDecodeError:
                pass
        # writer.close()
        cursor.close()
        db.close()

    def saveBigWordNatureData2DB(self):
        # 打开数据库连接
        db = pymysql.connect(host="192.168.1.105",user="root",password="admin",database="corpus" )
        cursor = db.cursor()
        path = "E:/BaiduNetdiskDownload/r"
        print(path)
        files = IOUtils.FileHelper.getFileAbsroutePathList(path)

        for file in files:
            print(file)
            reader= open(file, mode='r',encoding="utf-8")
            # writer = open("E:/BaiduNetdiskDownload/rm.txt",mode='w',encoding='utf-8')
            try:
                # print(reader.read())
                    # line= reader.read()
                lines = reader.readlines()
                for line in lines:
                    # print(line)
                    sline = line.strip()
                    if(len(line.strip())==0):
                        continue
                    idstr = sline[0:19].replace('-','')
                    sline = sline[21:].strip()
                    sline = rm.strQ2B(self,sline)
                    sline = rm.getBigWordLine(sline)
                    # print(sline)
                    print(len(idstr))
                    # writer.write(idstr+'\t'+sline+'\n')

                    # SQL 插入语句
                    sql = "INSERT INTO RenminRibao1998_BigWordNature(tid,text)VALUES ('%s', '%s')"%(idstr,sline)
                    print(sql)
                    try:
                        # 执行sql语句
                        cursor.execute(sql)
                        # 提交到数据库执行
                        db.commit()
                    except Exception as e:
                        # 如果发生错误则回滚
                        db.rollback()
                        print(str(e))
            except UnicodeDecodeError:
                pass
        # writer.close()
        cursor.close()
        db.close()



# if __name__ == '__main__':
#     ms = MySQLHelper()
#     ms.saveData2DB()