import os
import re
import sys
import string


'''代码参考了该博客https://blog.csdn.net/SueMagic/article/details/85539566
'''

def convert(s1,s2):
    if s1.isdigit():
        if int(s1)==12:
            s1="COVID-19_"+"Dec."
        elif int(s1)==1:
            s1="COVID-19_"+"Jan."
        elif int(s1)==2:
            s1="COVID-19_"+"Feb."
        elif int(s1)==3:
            s1="COVID-19_"+"Mar."
    if s2.isdigit():
        if int(s2)==12:
            s2="COVID-19_"+"Dec."
        elif int(s2)==1:
            s2="COVID-19_"+"Jan."
        elif int(s2)==2:
            s2="COVID-19_"+"Feb."
        elif int(s2)==3:
            s2="COVID-19_"+"Mar."
    print(s1,s2)
    return s1,s2


def main(dir):
    fileList = os.listdir(dir)
    # 输出此文件夹中包含的文件名称
    print("修改前：" + str(fileList)[1])
    # 得到进程当前工作目录
    currentpath = os.getcwd()
    # 将当前工作目录修改为待修改文件夹的位置
    os.chdir(dir)
    # 名称变量
    # 遍历文件夹中所有文件
    for fileName in fileList:
        # 文件重新命名
        s1,s2=convert(fileName.split("-")[0].strip(),fileName.split("-")[1].strip())
        os.rename(fileName,  s1 +"--" +s2)
        '''
        pat = ".+\.(xlsx)"#匹配要修改的文件格式
        pattern = re.findall(pat, fileName)
        os.rename(fileName, (str(num + 839) + '.' + pattern[0]))
        '''
        # 改变编号，继续下一项
    print("***************************************")
    # 改回程序运行前的工作目录
    os.chdir(currentpath)
    # 刷新
    sys.stdin.flush()
    # 输出修改后文件夹中包含的文件名称
    print("修改后：" + str(os.listdir(dir))[1])
main(".\testdata")