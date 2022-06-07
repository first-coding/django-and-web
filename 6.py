import requests
from bs4 import BeautifulSoup
from lxml import  etree
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
}
# 金融
url ="https://www.cnrencai.com/shuji/800078.html"
response=requests.get(url,headers=headers)
page_text=response.text
with open ("./jinrongshuji.html","w",encoding="utf-8") as fp:
    fp.write(page_text)
fp=open("./jinrongshuji.html","r",encoding="utf-8")
soup=BeautifulSoup(fp,"lxml")
sm=[]
for i in range(0,15):
    smm=soup.select("strong")[i].string
    smm="".join(smm.split())
    sm.append(smm)
print(sm)
for i in sm:
    print(i)


#金融
url6="https://baike.baidu.com/item/%E4%BC%9A%E8%AE%A1%E4%B8%93%E4%B8%9A/5279885?fr=aladdin"
response6=requests.get(url6,headers=headers)
page_text6=response6.text
with open ("./jinrongjieshao.html","w",encoding="utf-8") as fp6:
    fp6.write(page_text6)
fp6=open("./jinrongjieshao.html","r",encoding="utf-8")
soup=BeautifulSoup(fp6,"lxml")
sm6=[]
smm6=soup.find("div",class_="para").text
sm6.append(smm6)
print(sm6)


#金融
url16="https://ke.qq.com/course/list/%E4%BC%9A%E8%AE%A1"
response16 = requests.get(url16,headers).content.decode()
HTTP = etree.HTML(response16)
urls = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@href')
name = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@title')
print(name)
print(urls)

