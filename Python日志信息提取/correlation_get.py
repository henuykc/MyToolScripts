import os
import sys
import xlwt
import math




def read_one_file(filename,name):
    #此处根据日志特点进行提取适配
    job_str = open(filename).read()
    lines = job_str.splitlines()
    print(len(lines))
    # f = xlwt.Workbook()
    # sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet

    row_set=set()
    col_set=set()
    finalmap={}
    subMapList=[]
    count=0
    lastRow=' '
    #对finalmap初始化
    for line in lines:
        feature=[]
        values=line.split(" ")
        #插入序列长度信息
        feature.append([int(values[2].strip()),int(values[3].strip())])
        #插入LCS长度及相似度
        feature.append([int(values[4].strip()),float(values[5].strip())])
        #插入LD长度及相似度
        feature.append([int(values[6].strip()),float(values[7].strip())])
        row_set.add(values[0].strip())
        col_set.add(values[1].strip())
        index=values[0].strip()+values[1].strip()
        finalmap[index]=feature
    #     print(name)
    #     print(count)
    #     if (count%5==4):
    #         count += 1
    #         continue
    #     if(count%5==0):
    #         print(len(line.split(' ')))
    #         print(line.split(' '))
    #         row=line.split(' ')[0].strip()
    #         if row!=lastRow and lastRow!='':
    #             finalmap[lastRow]=subMapList
    #             subMapList=[]
    #             lastRow=row
    #         col=line.split(' ')[1].strip()
    #         count += 1
    #         continue
    #     if(count%5==1):
    #         feature.append([int(line.split(' ')[0].strip()),int(line.split(' ')[1].strip())])
    #         count += 1
    #         continue
    #     if(count%5==2):
    #         feature.append([int(line.split(' ')[0].strip()),float(line.split(' ')[1].strip())])
    #         count += 1
    #         continue
    #     if(count%5==3):
    #         feature.append([int(line.split(' ')[0].strip()), float(line.split(' ')[1].strip())])
    #         subMap[col] = feature
    #         subMapList.append(subMap)
    #         # finalmap[row] = subMap
    #         count += 1
    #         subMap={}
    #         feature=[]
    #         continue
    # finalmap[lastRow] = subMapList
    # sorted(finalmap.items(),key=lambda x:x[0])
    # for k,v in finalmap.items():
    #     finalmap[k]=v.sort()
    return row_set,col_set,finalmap

# def lsc_get(filename,file):
#     matrixMap=read_one_file(filename,file)
#     for key, value in matrixMap.items():
#         print(key + ':' + value)


def lcs_write(filename,name,f):

    sheet1 = f.add_sheet(name, cell_overwrite_ok=True)  # 创建sheet
    row_set,col_set,matrixMap=read_one_file(filename,name)
    print(matrixMap)
    # 将数据写入第 i 行，第 j 列
    i=1
    j=1
    #excel表格行是key，列是subkey
    count=0
    sum=0
    row_list=list(row_set)
    col_list=list(col_set)
    print(row_list)
    print(col_list)
    row_list.sort()
    col_list.sort()

    for row in row_list:
        sheet1.write(i,0,row)
        for col in col_list:
            index=row+col
            feature=matrixMap[index]
            #subList[0][0]为key长度，subList[0][1]为subkey长度
            #subList[1][0]为LCS长度，subList[1][1]为LCS相似度
            #subList[2][0]为Ld长度，subList[2][1]为Ld相似度
            sheet1.write(0,j,col)
            sheet1.write(i, j, feature[2][1])
            j+=1
            count+=1
            sum+=float(feature[2][1])
        j=1
        i+=1
    # for key,value in matrixMap.items():
    #     sheet1.write(i,0,key)
    #     if key==' ':
    #         continue
    #     for subDict in value:
    #         for subKey,subList in subDict.items():
    #             #subList[0][0]为key长度，subList[0][1]为subkey长度
    #             #subList[1][0]为LCS长度，subList[1][1]为LCS相似度
    #             #subList[2][0]为Ld长度，subList[2][1]为Ld相似度
    #             sheet1.write(0,j,subKey)
    #             sheet1.write(i, j, subList[2][1])
    #             j+=1
    #             count+=1
    #             sum+=float(subList[2][1])
    #     j=1
    #     i+=1
    if math.sqrt(count).is_integer() and name.split("--")[0].strip()==name.split("--")[1].strip():
        return float((sum-math.sqrt(count))/(count-math.sqrt(count)))
    else:
        return float(sum/count)


def main():
    logdir = "./testdata"
    viruses=os.listdir(logdir)

    for virus in viruses:
        txt_path = os.path.join(logdir, virus)
        months = os.listdir(txt_path)
        for month in months:
            current_file = os.path.join(txt_path, month)
            names = os.listdir(current_file)
            result_f=xlwt.Workbook()
            sheet2 = result_f.add_sheet("ldresult", cell_overwrite_ok=True)  # 创建sheet
            row=0
            col=1
            lastname=""
            for name in names:
                filename = os.path.join(current_file, name)
                f = xlwt.Workbook()
                # file.write(filename+'\n')
                result=lcs_write(filename,name,f)
                f.save("./LDresult/"+name+".xls")  # 保存文件
                if name.split("--")[0]!=lastname:
                    row+=3
                    col=1
                    lastname=name.split("--")[0]
                sheet2.write(row,0,name.split("--")[0])
                sheet2.write(row-1,col,name.split("--")[1])
                sheet2.write(row, col, result)
                col+=1

            result_f.save("./LDresult/"+"LDresult"+".xls")


if __name__ == '__main__':

    main()
