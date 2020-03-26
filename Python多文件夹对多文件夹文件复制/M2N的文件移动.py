import os
import shutil
import random

def CreateDir(path):
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)
        print(path+' 目录创建成功')
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
# def CopyFile(oldpath, newPath):
#     # 获取当前路径下的文件名，返回List
#     fileNames = os.listdir(oldpath)
#     for file in fileNames:
#         # 将文件命加入到当前文件路径后面
#         newDir = oldpath + '/' + file
#         # 如果是文件
#         if os.path.isfile(newDir):
#             print(newDir)
#             newFile = newPath + file
#             shutil.copyfile(newDir, newFile)
#         #如果不是文件，递归这个文件夹的路径
#         else:
#             CopyFile(newDir,newPath)
#

def CopyAll(source_path,target_path):
    #source_path中的文件全部复制到target_path
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path)


def Copy(oldDir,newDir,count):
    #将一个文件夹的问价随机挑选count个放入另一文件夹
    #当文件夹中文件少于count时则整个复制过去
    folders=os.listdir(oldDir)
    for folder in folders:
        newFolder=os.path.join(newDir,folder)
        CreateDir(newFolder)
        oldFolder=os.path.join(oldDir,folder)
        files=os.listdir(oldFolder)
        print(files)
        if count<len(files):
            for i in range(count):
                file=random.choice(files)
                print(file)
                oldfilepath=oldFolder+"/"+ file
                newfilepath=newFolder+"/"+ file
                shutil.copyfile(oldfilepath, newfilepath)

        else:
            CopyAll(oldFolder,newFolder)
            #全部复制过去
            # CopyFile(oldFolder,newFolder)


def one2one(oldDir,newDir):
    folders=os.listdir(oldDir)
    #以中国文件夹中的文件数作为分组的基准
    length=len(os.listdir(os.path.join(oldDir,"中国")))
    countryMap=dict()
    for folder in folders:
        countryMap[folder]=0
    for i in range(length):
        newFolder=newDir+"/"+ "sequence11_"+str(i)
        CreateDir(newFolder)
        for folder in folders:
            oldFolder=oldDir+"/"+folder
            files=os.listdir(oldFolder)
            file=files[countryMap[folder]%len(files)]
            oldfilepath=oldFolder+"/"+ file
            getInfo(oldfilepath)
            newfilepath=newFolder+"/"+ file
            # 将文件由oldfilepath复制到newfilepath
            shutil.copyfile(oldfilepath, newfilepath)
            countryMap[folder]+=1

def getInfo(file):
    job_str = open(file).read()
    lines = job_str.splitlines()
    for line in lines:
        if line.startswith(">"):
            print(line.split(">")[-1])



if __name__ == "__main__":
    #原始文件夹路径
    path = "./第九批进化树实验"
    # 目标文件夹路径
    mkPath = "./第10批进化树实验"
    # CreateDir(mkPath)
    # Copy(path,mkPath,3)
    one2one(path,mkPath)
    # listdir=os.listdir(path)
    # for dir in listdir:
    #     CopyAll(path+"/"+dir,mkPath)