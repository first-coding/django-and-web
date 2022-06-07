from django.http import JsonResponse
import  requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import  etree
from .models import *
# Create your views here.
def jinrongspider(request):
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
    print(len(sm))

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
    print(len(sm6))

    #金融
    url16="https://ke.qq.com/course/list/%E4%BC%9A%E8%AE%A1"
    response16 = requests.get(url16,headers).content.decode()
    HTTP = etree.HTML(response16)
    urls = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@href')
    name = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@title')
    print(len(urls))
    print(len(name))
    for i,j in zip(urls,name):
        economy.objects.create(Class=j,classurl=i)
    id=1
    for z in range(0,18,1):
        if(z==0):
            id = id + 0
        else:
            id = id + 1
        print(id)
        a = economy.objects.get(id=id)
        if(z<15):
            print(z)
            a.book = sm[z]
        if(z>15 or z==15):
            print(z)
            a.book = 'NULL'
        a.intro = sm6[0]
        a.save()

    return JsonResponse("ok",json_dumps_params={'ensure_ascii':False},safe=False)

def guanlispider(request):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
    }
    # 管理
    url2="https://zhuanlan.zhihu.com/p/443561380"
    response2=requests.get(url2,headers=headers)
    page_text2=response2.text
    with open ("./guanlishuji.html","w",encoding="utf-8") as fp2:
        fp2.write(page_text2)
    fp2=open("./guanlishuji.html","r",encoding="utf-8")
    soup=BeautifulSoup(fp2,"lxml")
    sm2=[]
    for z in range(0,5):
        smm2=soup.select("b")[z].string
        smm2="".join(smm2.split())
        sm2.append(smm2)
    print(sm2)

    #管理
    url17="https://ke.qq.com/course/list/%E7%AE%A1%E7%90%86"
    response17 = requests.get(url17,headers).content.decode()
    HTTP = etree.HTML(response17)
    urls = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@href')
    name = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@title')
    print(name)
    print(urls)

    #管理
    url9="https://baike.baidu.com/item/%E7%AE%A1%E7%90%86%E4%B8%93%E4%B8%9A/4026230?fr=aladdin"
    response9=requests.get(url9,headers=headers)
    page_text9=response9.text
    with open ("./guanlijieshao.html","w",encoding="utf-8") as fp9:
        fp9.write(page_text9)
    fp9=open("./guanlijieshao.html","r",encoding="utf-8")
    soup=BeautifulSoup(fp9,"lxml")
    sm9=[]
    smm9=soup.find("div",class_="para").text
    sm9.append(smm9)
    for i,j in zip(urls,name):
         manage.objects.create(Class=j,classurl=i)
    id=1
    for z in range(0,16,1):
        if(z==0):
            id = id + 0
        else:
            id = id + 1
        a = manage.objects.get(id=id)
        if(z<5):
            print(z)
            a.book = sm2[z]
        if(z>5 or z==5):
            print(z)
            a.book = 'NULL'
        a.intro = sm9[0]
        a.save()
    print(sm9[0])
    print(len(urls))
    print(len(name))
    print(len(sm9))
    print(len(sm2))
    return JsonResponse("ok",json_dumps_params={'ensure_ascii':False},safe=False)

def jisuanjispider(request):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
    }
    # 计算机
    url4="https://www.bilibili.com/read/cv13895872"
    response4=requests.get(url4,headers=headers)
    page_text4=response4.text
    with open ("./jisuanjishuji.html","w",encoding="utf-8") as fp4:
        fp4.write(page_text4)
    fp4=open("./jisuanjishuji.html","r",encoding="utf-8")
    soup=BeautifulSoup(fp4,"lxml")
    sm4=[]
    for l in range(3,14):
        smm4=soup.select("p")[l].string
        sm4.append(smm4)
    print(sm4)

    #计算机
    url7="https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6%E4%B8%8E%E6%8A%80%E6%9C%AF/663582?fr=aladdin"
    response7=requests.get(url7,headers=headers)
    page_text7=response7.text
    with open ("./jisuanjijieshao.html","w",encoding="utf-8") as fp7:
        fp7.write(page_text7)
    fp7=open("./jisuanjijieshao.html","r",encoding="utf-8")
    soup=BeautifulSoup(fp7,"lxml")
    sm7=[]
    smm7=soup.find("div",class_="para").text
    sm7.append(smm7)
    print(sm7)

    #计算机
    url13="https://ke.qq.com/course/list/%E8%AE%A1%E7%AE%97%E6%9C%BA"
    response13 = requests.get(url13,headers).content.decode()
    HTTP = etree.HTML(response13)
    urls = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@href')
    name = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@title')
    print(name)
    print(urls)
    for i in sm4:
        cs.objects.create(book=i)
    id=1
    for z in range(0,11,1):
        if(z==0):
            id = id + 0
        else:
            id = id + 1
        a = cs.objects.get(id=id)
        if(z<6):
            a.Class = name[z]
            a.classurl = urls[z]
        if(z>6 or z==6):
            a.Class= 'NULL'
            a.classurl = 'NULL'
        a.intro = sm7[0]
        a.save()
    return JsonResponse("ok",json_dumps_params={'ensure_ascii':False},safe=False)


def yuyanspider(request):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
    }
    # 语言
    url3="https://www.honglingjin.co.uk/226062.html"
    response5=requests.get(url3,headers=headers)
    page_text5=response5.text
    with open ("./yuyanshuji.html","w",encoding="utf-8") as fp5:
        fp5.write(page_text5)
    fp5=open("./yuyanshuji.html","r",encoding="utf-8")
    soup=BeautifulSoup(fp5,"lxml")
    sm5=[]
    for q in range(0,9):
        smm5=soup.select("h2")[q].string
        sm5.append(smm5)
    print(sm5)

    #外语
    url8="https://baike.baidu.com/item/%E8%8B%B1%E8%AF%AD/24600222?fromtitle=%E8%8B%B1%E8%AF%AD%E4%B8%93%E4%B8%9A&fromid=6091808&fr=aladdin"
    response8=requests.get(url8,headers=headers)
    page_text8=response8.text
    with open ("./yuyanjieshao.html","w",encoding="utf-8") as fp8:
        fp8.write(page_text8)
    fp8=open("./yuyanjieshao.html","r",encoding="utf-8")
    soup=BeautifulSoup(fp8,"lxml")
    sm8=[]
    smm8=soup.find("div",class_="para").text
    sm8.append(smm8)
    print(sm8)


    #外语
    url15 ='https://ke.qq.com/course/list/%E8%8B%B1%E8%AF%AD'
    response15 = requests.get(url15,headers).content.decode()
    HTTP = etree.HTML(response15)
    urls = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@href')
    name = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@title')
    print(name)
    print(urls)
    for i,j in zip(urls,name):
         english.objects.create(Class=j,classurl=i)
    id=1
    for z in range(0,15,1):
        if(z==0):
            id = id + 0
        else:
            id = id + 1
        a = english.objects.get(id=id)
        if(z<9):
            print(z)
            a.book = sm5[z]
        if(z>9 or z==9):
            print(z)
            a.book = 'NULL'
        a.intro = sm8[0]
        a.save()
    print(len(urls))
    print(len(name))
    print(len(sm5))
    print(len(sm8))

    return JsonResponse("ok",json_dumps_params={'ensure_ascii':False},safe=False)

def values(request):
    specifical= request.GET.get('data2')
    print(specifical)
    
    return JsonResponse("ok",json_dumps_params={'ensure_ascii':False},safe=False)

def computer(request):
    all = cs.objects.all().values()
    allchange = pd.DataFrame(all)
    id = list(allchange['id'])
    intro = list(allchange['intro'])
    book = list(allchange['book'])
    Class = list(allchange['Class'])
    classurl = list(allchange['classurl'])
    data = {
        'id':id,
        'intro':intro,
        'book':book,
        'Class':Class,
        'classurl':classurl
    }
    # print(data)
    return JsonResponse(data,json_dumps_params={'ensure_ascii':False},safe=False)


def economys(request):
    all = economy.objects.all().values()
    allchange = pd.DataFrame(all)
    id = list(allchange['id'])
    intro = list(allchange['intro'])
    book = list(allchange['book'])
    Class = list(allchange['Class'])
    classurl = list(allchange['classurl'])
    data = {
        'id':id,
        'intro':intro,
        'book':book,
        'Class':Class,
        'classurl':classurl
    }
    # print(data)
    return JsonResponse(data,json_dumps_params={'ensure_ascii':False},safe=False)

#
def English(request):
    all = english.objects.all().values()
    allchange = pd.DataFrame(all)
    id = list(allchange['id'])
    intro = list(allchange['intro'])
    book = list(allchange['book'])
    Class = list(allchange['Class'])
    classurl = list(allchange['classurl'])
    data = {
        'id':id,
        'intro':intro,
        'book':book,
        'Class':Class,
        'classurl':classurl
    }
    return JsonResponse(data,json_dumps_params={'ensure_ascii':False},safe=False)

def manages(request):
    all = manage.objects.all().values()
    allchange = pd.DataFrame(all)
    id = list(allchange['id'])
    intro = list(allchange['intro'])
    book = list(allchange['book'])
    Class = list(allchange['Class'])
    classurl = list(allchange['classurl'])
    data = {
        'id':id,
        'intro':intro,
        'book':book,
        'Class':Class,
        'classurl':classurl
    }
    # print(data)
    return JsonResponse(data,json_dumps_params={'ensure_ascii':False},safe=False)
#

def test(request):
    first = request.GET.get('id')
    return "ok"
