import requests
import time 
from bs4 import BeautifulSoup as BS
import xlwt
import xlrd
import os
import re

url = "http://gaokao.chsi.com.cn/zsgs/bssnlqmd--method-groupByYx.dhtml"

#get_html()使用requests.get() 获取html文本
def get_html(url):
    try:
        res = requests.get(url,timeout=30)
        res.encoding = "utf-8"
        return res.text
    except:
        return "ERROR"
    
#获取当前页面的所有的url，存入lsit    
def get_url(url):
    html = get_html(url)
    soup = BS(html,"html.parser")
    content = soup.find_all("li")
    content_2 = content[4:]
    url_list = []
    for i in content_2:
        u = i.a["href"]
        l = "http://gaokao.chsi.com.cn"+u
        url_list.append(l)
    return url_list

#获取具体页面的内容，使用BeautifulSoup
def get_content(url):
    html = get_html(url)
    soup = BS(html,"html.parser")
    
 #获取标题,使用re.split切分
    table_name = re.split(r"[\(,\)]",soup.h2.text)[1]
    
#获取内容
    name = soup.find_all("td")[::8]
    sex = soup.find_all("td")[1::8]
    province = soup.find_all("td")[2::8]
    school = soup.find_all("td")[3::8]
    Features = soup.find_all("td")[4::8]
    score = soup.find_all("td")[5::8]
    check = soup.find_all("td")[6::8]
    specialty = soup.find_all("td")[7::8]
    
#创建工作表
    #data = xlwt.Workbook()
    table_name = data.add_sheet(table_name)
    
#将网页获取到的内容存入dict
    dict = {}
    for i in range(len(sex)):
        dict[i+1]=[name[i].text,sex[i].text,province[i].text,school[i].text,re.sub('[\t\n\r]',"",Features[i].text),score[i].text,check[i].text,specialty[i].text,]
    
#将dict 转化为list,把key写到里面。
    ldict = []    
    num = [a for a in dict]
    num.sort()
    for x in num:
        t = [int(x)]
        for i in dict[x]:
            t.append(i)
        ldict.append(t)
        
#将内容list 使用enumerate传入 sheet
    for i,p in enumerate(ldict):
        for j,q in enumerate(p):
            table_name.write(i,j,q)
            #print(i,j,q)
    
    data.save(u"e:\\beijingschool.xls")
    
    

if __name__ == "__main__":
    data = xlwt.Workbook()
    for u in get_url(url):
        get_content(u)
    print("爬取完成")
        
    


