import os
import os.path #文件夹遍历函数
#获取目标文件夹的路径
def merge_file(files_path,file_format):
    #获取当前文件夹中的文件名称列表
    filenames=os.listdir(files_path)
    #打开当前目录下的result.txt文件，如果没有则创建
    final_name=files_path.split("/")[-1]
    file_path=''
    for i in range(len(files_path.split("/"))):
        if i < len(files_path.split("/"))-1:
            file_path+=files_path.split("/")[i]
    f=open(file_path+"/"+final_name+file_format,'w')
    #先遍历文件名
    for filename in filenames:
        filepath = files_path+'/'+filename
        #遍历单个文件，读取行数
        for line in open(filepath):
            f.writelines(line)
        f.write('\n')
    #关闭文件
    f.close()

def main():
    merge_path=".\/new"
    file_format=".fasta"
    filesname=os.listdir(merge_path)
    for files in filesname:
        merge_file(merge_path+"/"+files,file_format)
main()