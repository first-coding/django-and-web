from django.http import JsonResponse
import requests
import pandas as pd
from bs4 import BeautifulSoup
from django.shortcuts import render
from lxml import etree
from .models import *
from django.http import HttpResponse
import requests
import urllib.parse
from lxml import etree
import re
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter('ignore')
def jinrongspider(request):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
    }
    # 金融
    url = "https://www.cnrencai.com/shuji/800078.html"
    response = requests.get(url, headers=headers)
    page_text = response.text
    with open("./jinrongshuji.html", "w", encoding="utf-8") as fp:
        fp.write(page_text)
    fp = open("./jinrongshuji.html", "r", encoding="utf-8")
    soup = BeautifulSoup(fp, "lxml")
    sm = []
    for i in range(0, 15):
        smm = soup.select("strong")[i].string
        smm = "".join(smm.split())
        sm.append(smm)
    print(len(sm))

    # 金融
    url6 = "https://baike.baidu.com/item/%E4%BC%9A%E8%AE%A1%E4%B8%93%E4%B8%9A/5279885?fr=aladdin"
    response6 = requests.get(url6, headers=headers)
    page_text6 = response6.text
    with open("./jinrongjieshao.html", "w", encoding="utf-8") as fp6:
        fp6.write(page_text6)
    fp6 = open("./jinrongjieshao.html", "r", encoding="utf-8")
    soup = BeautifulSoup(fp6, "lxml")
    sm6 = []
    smm6 = soup.find("div", class_="para").text
    sm6.append(smm6)
    print(len(sm6))

    # 金融
    url16 = "https://ke.qq.com/course/list/%E4%BC%9A%E8%AE%A1"
    response16 = requests.get(url16, headers).content.decode()
    HTTP = etree.HTML(response16)
    urls = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@href')
    name = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@title')
    print(len(urls))
    print(len(name))
    for i, j in zip(urls, name):
        economy.objects.create(Class=j, classurl=i)
    id = 1
    for z in range(0, 18, 1):
        if (z == 0):
            id = id + 0
        else:
            id = id + 1
        print(id)
        a = economy.objects.get(id=id)
        if (z < 15):
            print(z)
            a.book = sm[z]
        if (z > 15 or z == 15):
            print(z)
            a.book = 'NULL'
        a.intro = sm6[0]
        a.save()

    return JsonResponse("ok", json_dumps_params={'ensure_ascii': False}, safe=False)
def guanlispider(request):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
    }
    # 管理
    url2 = "https://zhuanlan.zhihu.com/p/443561380"
    response2 = requests.get(url2, headers=headers)
    page_text2 = response2.text
    with open("./guanlishuji.html", "w", encoding="utf-8") as fp2:
        fp2.write(page_text2)
    fp2 = open("./guanlishuji.html", "r", encoding="utf-8")
    soup = BeautifulSoup(fp2, "lxml")
    sm2 = []
    for z in range(0, 5):
        smm2 = soup.select("b")[z].string
        smm2 = "".join(smm2.split())
        sm2.append(smm2)
    print(sm2)

    # 管理
    url17 = "https://ke.qq.com/course/list/%E7%AE%A1%E7%90%86"
    response17 = requests.get(url17, headers).content.decode()
    HTTP = etree.HTML(response17)
    urls = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@href')
    name = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@title')
    print(name)
    print(urls)

    # 管理
    url9 = "https://baike.baidu.com/item/%E7%AE%A1%E7%90%86%E4%B8%93%E4%B8%9A/4026230?fr=aladdin"
    response9 = requests.get(url9, headers=headers)
    page_text9 = response9.text
    with open("./guanlijieshao.html", "w", encoding="utf-8") as fp9:
        fp9.write(page_text9)
    fp9 = open("./guanlijieshao.html", "r", encoding="utf-8")
    soup = BeautifulSoup(fp9, "lxml")
    sm9 = []
    smm9 = soup.find("div", class_="para").text
    sm9.append(smm9)
    for i, j in zip(urls, name):
        managee.objects.create(Class=j, classurl=i)
    user_id = 1
    for z in range(0, 21, 1):
        if (z == 0):
            user_id = user_id + 0
        else:
            user_id = user_id + 1
        a = managee.objects.get(user_id=user_id)
        if (z < 5):
            print(z)
            a.book = sm2[z]
        if (z > 5 or z == 5):
            print(z)
            a.book = 'NULL'
        a.intro = sm9[0]
        a.save()
    print(sm9[0])
    print(len(urls))
    print(len(name))
    print(len(sm9))
    print(len(sm2))
    return JsonResponse("ok", json_dumps_params={'ensure_ascii': False}, safe=False)
def jisuanjispider(request):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
    }
    # 计算机
    url4 = "https://www.bilibili.com/read/cv13895872"
    response4 = requests.get(url4, headers=headers)
    page_text4 = response4.text
    with open("./jisuanjishuji.html", "w", encoding="utf-8") as fp4:
        fp4.write(page_text4)
    fp4 = open("./jisuanjishuji.html", "r", encoding="utf-8")
    soup = BeautifulSoup(fp4, "lxml")
    sm4 = []
    for l in range(3, 14):
        smm4 = soup.select("p")[l].string
        sm4.append(smm4)
    print(sm4)

    # 计算机
    url7 = "https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6%E4%B8%8E%E6%8A%80%E6%9C%AF/663582?fr=aladdin"
    response7 = requests.get(url7, headers=headers)
    page_text7 = response7.text
    with open("./jisuanjijieshao.html", "w", encoding="utf-8") as fp7:
        fp7.write(page_text7)
    fp7 = open("./jisuanjijieshao.html", "r", encoding="utf-8")
    soup = BeautifulSoup(fp7, "lxml")
    sm7 = []
    smm7 = soup.find("div", class_="para").text
    sm7.append(smm7)
    print(sm7)

    # 计算机
    url13 = "https://ke.qq.com/course/list/%E8%AE%A1%E7%AE%97%E6%9C%BA"
    response13 = requests.get(url13, headers).content.decode()
    HTTP = etree.HTML(response13)
    urls = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@href')
    name = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@title')
    print(name)
    print(urls)
    for i in sm4:
        cs.objects.create(book=i)
    id = 1
    for z in range(0, 11, 1):
        if (z == 0):
            id = id + 0
        else:
            id = id + 1
        a = cs.objects.get(id=id)
        if (z < 6):
            a.Class = name[z]
            a.classurl = urls[z]
        if (z > 6 or z == 6):
            a.Class = 'NULL'
            a.classurl = 'NULL'
        a.intro = sm7[0]
        a.save()
    return JsonResponse("ok", json_dumps_params={'ensure_ascii': False}, safe=False)
def yuyanspider(request):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"
    }
    # 语言
    url3 = "https://www.honglingjin.co.uk/226062.html"
    response5 = requests.get(url3, headers=headers)
    page_text5 = response5.text
    with open("./yuyanshuji.html", "w", encoding="utf-8") as fp5:
        fp5.write(page_text5)
    fp5 = open("./yuyanshuji.html", "r", encoding="utf-8")
    soup = BeautifulSoup(fp5, "lxml")
    sm5 = []
    for q in range(0, 9):
        smm5 = soup.select("h2")[q].string
        sm5.append(smm5)
    print(sm5)

    # 外语
    url8 = "https://baike.baidu.com/item/%E8%8B%B1%E8%AF%AD/24600222?fromtitle=%E8%8B%B1%E8%AF%AD%E4%B8%93%E4%B8%9A&fromid=6091808&fr=aladdin"
    response8 = requests.get(url8, headers=headers)
    page_text8 = response8.text
    with open("./yuyanjieshao.html", "w", encoding="utf-8") as fp8:
        fp8.write(page_text8)
    fp8 = open("./yuyanjieshao.html", "r", encoding="utf-8")
    soup = BeautifulSoup(fp8, "lxml")
    sm8 = []
    smm8 = soup.find("div", class_="para").text
    sm8.append(smm8)
    print(sm8)

    # 外语
    url15 = 'https://ke.qq.com/course/list/%E8%8B%B1%E8%AF%AD'
    response15 = requests.get(url15, headers).content.decode()
    HTTP = etree.HTML(response15)
    urls = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@href')
    name = HTTP.xpath('//h4[@class="item-tt item-tt--oneline"]/a/@title')
    print(name)
    print(urls)
    for i, j in zip(urls, name):
        english.objects.create(Class=j, classurl=i)
    id = 1
    for z in range(0, 15, 1):
        if (z == 0):
            id = id + 0
        else:
            id = id + 1
        a = english.objects.get(id=id)
        if (z < 9):
            print(z)
            a.book = sm5[z]
        if (z > 9 or z == 9):
            print(z)
            a.book = 'NULL'
        a.intro = sm8[0]
        a.save()
    print(len(urls))
    print(len(name))
    print(len(sm5))
    print(len(sm8))

    return JsonResponse("ok", json_dumps_params={'ensure_ascii': False}, safe=False)
def computer(request):
    all = cs.objects.all().values()
    allchange = pd.DataFrame(all)
    id = list(allchange['id'])
    intro = list(allchange['intro'])
    book = list(allchange['book'])
    Class = list(allchange['Class'])
    classurl = list(allchange['classurl'])
    data = {
        'id': id,
        'intro': intro,
        'book': book,
        'Class': Class,
        'classurl': classurl
    }
    # print(data)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, safe=False)
def economys(request):
    all = economy.objects.all().values()
    allchange = pd.DataFrame(all)
    id = list(allchange['id'])
    intro = list(allchange['intro'])
    book = list(allchange['book'])
    Class = list(allchange['Class'])
    classurl = list(allchange['classurl'])
    data = {
        'id': id,
        'intro': intro,
        'book': book,
        'Class': Class,
        'classurl': classurl
    }
    # print(data)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, safe=False)
def English(request):
    all = english.objects.all().values()
    allchange = pd.DataFrame(all)
    id = list(allchange['id'])
    intro = list(allchange['intro'])
    book = list(allchange['book'])
    Class = list(allchange['Class'])
    classurl = list(allchange['classurl'])
    data = {
        'id': id,
        'intro': intro,
        'book': book,
        'Class': Class,
        'classurl': classurl
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, safe=False)
def manages(request):
    all = managee.objects.all().values()
    allchange = pd.DataFrame(all)
    id = list(allchange['user_id'])
    intro = list(allchange['intro'])
    book = list(allchange['book'])
    Class = list(allchange['Class'])
    classurl = list(allchange['classurl'])
    data = {
        'id': id,
        'intro': intro,
        'book': book,
        'Class': Class,
        'classurl': classurl
    }
    # print(data)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False}, safe=False)
def Login_view(request):
    user = request.GET.get('user', '')
    pwd = request.GET.get('pwd', '')

    if user and pwd:
        c = manage.objects.filter(user_name=user, user_pwd=pwd).count()
        # for data in list(USERInfo.objects.filter(user_name=u,user_pwd=p)):
        #     print('----------')
        #     print(data.user_name)
        print(user)
        print(pwd)
        if c == 1:
            return HttpResponse('登录成功')
        else:
            return HttpResponse('登录失败')
    else:
        return HttpResponse('登录失败')
def register(request):
    user = request.GET.get('user', '')
    pwd = request.GET.get('pwd', '')
    print(user)
    print(pwd)
    if user and pwd:
        manage.objects.create(user_name=user, user_pwd=pwd)
        c = manage.objects.filter(user_name=user).count()
        if c == 1:
            return HttpResponse('注册成功')
        else:
            return HttpResponse('注册失败')
    else:
        return HttpResponse('注册失败')
def pagenumber(request):
    work = request.GET.get('work')
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
        'cookie': 'gr_user_id=0f3bb2ed-acd9-454d-80aa-457d6e6def6a; RANGERS_SAMPLE=0.014220170471998417; RANGERS_WEB_ID=usr_b6ythlwgcp7u; utm_campaign=baidusem; utm_source=sem-baidu-pc-pinpai-4; utm_source_first=sem-baidu-pc-pinpai-4; gr_cs1_61ce3d36-ac25-4b76-99f1-2805ed1fedaf=user_id%3Anull; SXS_XSESSION_ID=2|1:0|10:1652057629|15:SXS_XSESSION_ID|88:ZDJjNDk5ZWY1NWRhZTFmM2Q4Yjg0YjcxMDljM2ZlMzU2Yzc2M2ZiNjg1ZjMyNjFmZDAyMzI3NDVjNTZmZmVkYg==|f9ef6cbae28991bc043bcce5673609825c03d669297fd01bab664681184c4e89; SXS_XSESSION_ID_EXP=2|1:0|10:1652057629|19:SXS_XSESSION_ID_EXP|16:MTY1NDY0OTYyOQ==|7c05a3624f0f3809a4c454ce2abfba257e410a0b718337dcecb04c7c14f781b2; affefdgx=usr_b6ythlwgcp7u; sxs_usr=2|1:0|10:1652057629|7:sxs_usr|24:dXNyX2I2eXRobHdnY3A3dQ==|2f18f904a2ff28e68f4f9fc81cfd7df45ac84415f0dd5723c964f542be474ed4; xyz_usr=2|1:0|10:1652057629|7:xyz_usr|40:bzhSbncwQzRidWhXZ0pmZjNzT3BjbnhsN1NESQ==|b09faeaa5939fc219b4ecedcfd348bf31866a67f27310a921520fa8c8c6e9664; userflag=user; gr_session_id_96145fbb44e87b47=e2fe117f-0b19-4333-b32c-d0a47dbb7fad; gr_cs1_e2fe117f-0b19-4333-b32c-d0a47dbb7fad=user_id%3Ausr_b6ythlwgcp7u; Hm_lvt_03465902f492a43ee3eb3543d81eba55=1649934610,1652057631; gr_session_id_96145fbb44e87b47_e2fe117f-0b19-4333-b32c-d0a47dbb7fad=true; adCloseOpen=true; Hm_lpvt_03465902f492a43ee3eb3543d81eba55=1652058027'
    }
    work = work
    work_urlencode = urllib.parse.quote(work)
    url = 'https://www.shixiseng.com/interns?page=1&type=intern&keyword={}&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend='.format(
        work_urlencode)
    response = requests.get(url, header).text
    data_HTML = etree.HTML(response)
    number = data_HTML.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[8]/text()')[0]
    return JsonResponse(number,json_dumps_params={'ensure_ascii': False}, safe=False)

class Get_data():
    def __init__(self,jok,page,work):
        self.work=work
        self.jok = jok
        self.page = page
        self.header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
                'cookie': 'gr_user_id=0f3bb2ed-acd9-454d-80aa-457d6e6def6a; RANGERS_SAMPLE=0.014220170471998417; RANGERS_WEB_ID=usr_b6ythlwgcp7u; utm_campaign=baidusem; utm_source=sem-baidu-pc-pinpai-4; utm_source_first=sem-baidu-pc-pinpai-4; gr_cs1_61ce3d36-ac25-4b76-99f1-2805ed1fedaf=user_id%3Anull; SXS_XSESSION_ID=2|1:0|10:1652057629|15:SXS_XSESSION_ID|88:ZDJjNDk5ZWY1NWRhZTFmM2Q4Yjg0YjcxMDljM2ZlMzU2Yzc2M2ZiNjg1ZjMyNjFmZDAyMzI3NDVjNTZmZmVkYg==|f9ef6cbae28991bc043bcce5673609825c03d669297fd01bab664681184c4e89; SXS_XSESSION_ID_EXP=2|1:0|10:1652057629|19:SXS_XSESSION_ID_EXP|16:MTY1NDY0OTYyOQ==|7c05a3624f0f3809a4c454ce2abfba257e410a0b718337dcecb04c7c14f781b2; affefdgx=usr_b6ythlwgcp7u; sxs_usr=2|1:0|10:1652057629|7:sxs_usr|24:dXNyX2I2eXRobHdnY3A3dQ==|2f18f904a2ff28e68f4f9fc81cfd7df45ac84415f0dd5723c964f542be474ed4; xyz_usr=2|1:0|10:1652057629|7:xyz_usr|40:bzhSbncwQzRidWhXZ0pmZjNzT3BjbnhsN1NESQ==|b09faeaa5939fc219b4ecedcfd348bf31866a67f27310a921520fa8c8c6e9664; userflag=user; gr_session_id_96145fbb44e87b47=e2fe117f-0b19-4333-b32c-d0a47dbb7fad; gr_cs1_e2fe117f-0b19-4333-b32c-d0a47dbb7fad=user_id%3Ausr_b6ythlwgcp7u; Hm_lvt_03465902f492a43ee3eb3543d81eba55=1649934610,1652057631; gr_session_id_96145fbb44e87b47_e2fe117f-0b19-4333-b32c-d0a47dbb7fad=true; adCloseOpen=true; Hm_lpvt_03465902f492a43ee3eb3543d81eba55=1652058027'
                }
        self.jok_name_list = []
        self.salary_list = []
        self.education_list = []
        self.internship_list = []
        self.work_place_list = []
        self.duty_list = []  # 职责
        self.requirement_list = []  # 要求
        self.become_a_regular_regular_worker = []
    def get_url(self):
        try:
            for pa in range(1,int(self.page)+1):
                url = 'https://www.shixiseng.com/interns?page={}&type=intern&keyword={}&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend='.format(pa,self.jok)
                response = requests.get(url, self.header).text
                data_HTML = etree.HTML(response)
                urls = data_HTML.xpath('//div[@class="f-l intern-detail__job"]//a/@href')
                for url_new in urls:
                    response = requests.get(url_new,self.header).text
                    data_HTML = etree.HTML(response)
                    job_name = data_HTML.xpath('//div[@class="new_job_name"]/span/text()')
                    salary = data_HTML.xpath('//span[@class="job_money cutom_font"]/text()')
                    education = data_HTML.xpath('//span[@class="job_academic"]/text()')
                    internship_time = data_HTML.xpath('//span[@class="job_time cutom_font"]/text()')  #获取实习时长和是否有转正机会
                    work_place = data_HTML.xpath('//div[@class="job_msg"]/span/@title')
                    position_detailed = ''.join(data_HTML.xpath('//div[@class="job_detail"]//text()')).replace("\n", "").replace('	','')
                    self.jok_name_list.append(job_name[0])
                    self.salary_list.append(salary[0])
                    self.education_list.append(education[0])
                    self.internship_list.append(internship_time[0])
                    self.work_place_list.append(work_place[0])
                    #匹配职责
                    gz = re.compile('职责(.*?)。 ')
                    gz1 = re.compile('职位描述(.*?)。')
                    #匹配要求
                    gz2 = re.compile('要求(.*?)。')
                    gz3 = re.compile('资格(.*?)。')
                    if gz.findall(position_detailed) != []:
                        self.duty_list.append(gz.findall(position_detailed)[0])
                    elif gz1.findall(position_detailed) != []:
                        self.duty_list.append(gz1.findall(position_detailed)[0])
                    else:
                        self.duty_list.append('')
                    if gz2.findall(position_detailed) != []:
                        self.requirement_list.append(gz2.findall(position_detailed)[0])
                    elif gz3.findall(position_detailed) != []:
                        self.requirement_list.append(gz3.findall(position_detailed[0]))
                    else:
                        self.requirement_list.append('')
                    if len(internship_time)==2:
                        self.become_a_regular_regular_worker.append('是')
                    else:
                        self.become_a_regular_regular_worker.append('否')
                    # time.sleep(1)#休息一秒
                print('爬取第{}页完成'.format(pa))
                # time.sleep(1)  # 休息一秒
                self.store_data()
        except:
            print('结束')
    def store_data(self):
        work = self.work
        job_name =self.jok_name_list
        salary = self.salary_list
        education = self.education_list
        internship_time = self.internship_list
        work_place=self.work_place_list
        duty_list = self.duty_list
        requirement_list=self.requirement_list
        becom_a_regular_worker = self.requirement_list
        data = {
            '岗位':job_name,
            '薪水':salary,
            '学历要求':education,
            '实习时长':internship_time,
            '上班地点':work_place,
            '职责':duty_list,
            '要求':requirement_list,
            '是否提供转正机会':becom_a_regular_worker
        }
        import pandas as pd
        df =pd.DataFrame(data)
        df.to_csv('./data/{}招聘信息.csv'.format(work),index=False)
        return df


class analysis():
    def __init__(self,data,word):
        self.data=data
        self.word=word
    def main(self):
        # 筛选
        data = self.data
        word = self.word
        data_new = data[data['岗位'].str.contains(word)]
        # 绘图
        education = data_new.groupby('学历要求').size()
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.subplot(1, 2, 1)
        plt.title('{}岗位'.format(word))
        plt.bar(education.index, education.values)
        plt.subplot(1, 2, 2)
        plt.title('{}岗位'.format(word))
        plt.pie(education.values, labels=education.index, autopct='%.2f%%')
        plt.savefig('./static/img/{}学历要求.png'.format(word))
        plt.close()


        work_place = data_new.groupby(by='上班地点').size().sort_values(ascending=False).head(5)
        plt.subplot(1, 2, 1)
        plt.title('{}岗位'.format(word))
        plt.bar(work_place.index, work_place.values)
        plt.subplot(1, 2, 2)
        plt.title('{}岗位'.format(word))
        plt.pie(work_place.values, labels=work_place.index, autopct='%.2f%%')
        plt.savefig('./static/img/{}上班地点.png'.format(word))
        # plt.show()

        def zh(x):
            if x=='面议':
                return int(0)
            else:
                return int(x.split('/')[0].split('-')[0])
        #拿薪资
        data_new['薪水'] =data_new['薪水'].apply(lambda x: zh(x))
        Max = data_new['薪水'].max()
        Min = data_new['薪水'].min()
        Mean = round(data_new['薪水'].mean(),2)
        # 文本分析
        import jieba
        analysis_duty = data_new.fillna(',')
        analysis_duty = analysis_duty.replace({'要求':{'[]': ','}})

        duty_str = ''.join(list(analysis_duty['要求']))
        zz_str = ''.join(list(analysis_duty['职责']))
        cut = jieba.lcut_for_search(duty_str)
        cut1 = jieba.lcut_for_search(zz_str)
        stopword = pd.read_csv('./data/work_word.txt', sep='bingrong', header=None, encoding='utf-8')
        # 去停用词
        stop = stopword.values
        stop = stop.ravel()

        cut = [x for x in cut if x not in stop]
        cut1 = [x for x in cut1 if x not in stop]

        # 绘画词云图

        from wordcloud import WordCloud
        import imageio
        st = ' '.join(cut)
        st1 = ' '.join(cut1)
        back_color = imageio.imread('./data/1.jpg')
        back_color1 = imageio.imread('./data/1.jpg')
        w = WordCloud(
            font_path='simhei.ttf',
            background_color='white',
            mask=back_color
        )
        w1 = WordCloud(
            font_path='simhei.ttf',
            background_color='white',
            mask=back_color1
        )
        w.generate(st)
        w1.generate(st1)
        w.to_file('./static/img/{}要求.png'.format(word))
        w1.to_file('./static/img/{}职责.png'.format(word))

        return Max,Min, Mean



def usemain(request):
    num=request.GET.get("num")
    work=request.GET.get("work")
    page=request.GET.get("page")
    if work == "计算机科学与技术":
        work="软件开发"
    # print(num,work,page)
    mains(num,work,page)
    ssss = {
        'data': "qwer"
    }
    return JsonResponse(ssss, json_dumps_params={'ensure_ascii': False}, safe=False)

def mains(num,work,page):
    num = num
    work = work
    page = page
    print(num)
    print(work)
    print(page)
    if num =='1':
        header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
                'cookie': 'gr_user_id=0f3bb2ed-acd9-454d-80aa-457d6e6def6a; RANGERS_SAMPLE=0.014220170471998417; RANGERS_WEB_ID=usr_b6ythlwgcp7u; utm_campaign=baidusem; utm_source=sem-baidu-pc-pinpai-4; utm_source_first=sem-baidu-pc-pinpai-4; gr_cs1_61ce3d36-ac25-4b76-99f1-2805ed1fedaf=user_id%3Anull; SXS_XSESSION_ID=2|1:0|10:1652057629|15:SXS_XSESSION_ID|88:ZDJjNDk5ZWY1NWRhZTFmM2Q4Yjg0YjcxMDljM2ZlMzU2Yzc2M2ZiNjg1ZjMyNjFmZDAyMzI3NDVjNTZmZmVkYg==|f9ef6cbae28991bc043bcce5673609825c03d669297fd01bab664681184c4e89; SXS_XSESSION_ID_EXP=2|1:0|10:1652057629|19:SXS_XSESSION_ID_EXP|16:MTY1NDY0OTYyOQ==|7c05a3624f0f3809a4c454ce2abfba257e410a0b718337dcecb04c7c14f781b2; affefdgx=usr_b6ythlwgcp7u; sxs_usr=2|1:0|10:1652057629|7:sxs_usr|24:dXNyX2I2eXRobHdnY3A3dQ==|2f18f904a2ff28e68f4f9fc81cfd7df45ac84415f0dd5723c964f542be474ed4; xyz_usr=2|1:0|10:1652057629|7:xyz_usr|40:bzhSbncwQzRidWhXZ0pmZjNzT3BjbnhsN1NESQ==|b09faeaa5939fc219b4ecedcfd348bf31866a67f27310a921520fa8c8c6e9664; userflag=user; gr_session_id_96145fbb44e87b47=e2fe117f-0b19-4333-b32c-d0a47dbb7fad; gr_cs1_e2fe117f-0b19-4333-b32c-d0a47dbb7fad=user_id%3Ausr_b6ythlwgcp7u; Hm_lvt_03465902f492a43ee3eb3543d81eba55=1649934610,1652057631; gr_session_id_96145fbb44e87b47_e2fe117f-0b19-4333-b32c-d0a47dbb7fad=true; adCloseOpen=true; Hm_lpvt_03465902f492a43ee3eb3543d81eba55=1652058027'
                }
        work=work
        work_urlencode = urllib.parse.quote(work)
        url = 'https://www.shixiseng.com/interns?page=1&type=intern&keyword={}&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend='.format(work_urlencode)
        response = requests.get(url,header).text
        data_HTML = etree.HTML(response)
        print('共有',data_HTML.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/ul/li[8]/text()')[0],'页')
        page=page
        # 实例化对象
        first = Get_data(work_urlencode, page,work)
        first.get_url()
        first.store_data()
        print('进行数据分析')
        data = pd.read_csv('./data/{}招聘信息.csv'.format(work))
        Analysis = analysis(data,work)
        Analysis.main()
        # 返回薪资三个值
        ssss ={
            'data':"ok"
        }
        return JsonResponse(ssss,json_dumps_params={'ensure_ascii': False}, safe=False)

    else:

        word = input('岗位名：')
        data = pd.read_csv('./data/{}招聘信息.csv'.format(word))
        Analysis = analysis(data,word)
        Analysis.main()
        #返回薪资三个值
        sssss ={
            'data':"error"
        }
        return JsonResponse(sssss,json_dumps_params={'ensure_ascii': False}, safe=False)

def imgg(request):
    n=request.GET.get("n")
    l=[]
    a=img.objects.filter(name=n).values()
    a=list(a)
    for i in range(0,len(a)):
        l.append(a[i]['img'])
    data = {
        'img':l
    }
    print(data)
    return JsonResponse(data,json_dumps_params={'ensure_ascii': False}, safe=False)
