#Ice Cream
import re

#去除空行函数
def rn(str):
    str1 = re.sub(r"[ ,\n]","",str)
    return str1 != ""

#创建两个文件夹
f = open("E:/desktop/1.txt","r",encoding = "utf-8")
w = open("E:/desktop/LM-L808C.txt","w")
#将所有行获取添加到list.
l = []
for i in f.readlines():
    l.append(i)
#使用 filter 剔除空行   ，并 打印行数
l1 = list(filter(rn,l))
print(len(l1))

#剔除后的lsit 内容写入新文件
for i in l1:
    w.write(i)

#关闭文件
f.close()
w.close()


