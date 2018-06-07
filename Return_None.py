#将空格删除掉
import re

def Return_None(str):
    str1 = re.sub(" ","",str)
    return str1 != ""


