


import requests
import re
import datetime

import sys
from tqdm import tqdm
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import time

"""
用来爬取东方财富的研报数据（必须要动态）
"""

#使用datetime来获取日期
now_time = datetime.datetime.now()
date=[]
endday=60#从今天开始到之后的第几天结束
for i in range(1,endday):
    yes_time = now_time + datetime.timedelta(days=-(endday-1)+i)
    date.append(yes_time.strftime('%m-%d'))


all_stock=[]
stock_dict={}
page=30#爬取到的最大页数
for i in tqdm(range(1,page)):
    browser = webdriver.Chrome()
    browser.get("http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0x")
    element = browser.find_element_by_id("gopage")#找到输入框
    element.clear()
    element.send_keys(str(i))
    # print(i)
    e = browser.find_element_by_xpath('//a[@class="btn_link"]')#找到翻页确定按钮*注：xpath这种方法可以对于所有标签，不只是div,span这种
    e.click()
    handles = browser.window_handles
    browser.switch_to.window(handles[0])#返回第一个打开的窗户
    time.sleep(5)#等待页面加载，若不等待则可能没有加载完成，这里可以使用显示或者隐式等待来代替sleep等待
    content = browser.page_source#获取当前页面的源代码
    browser.close()
    pattern1 = re.compile(
        'class="txt">(.*?)</span></td><td><a href=".*?" class="hqPopCls" data_code=".*?" data_name="(.*?)"', re.S)#正则其实比bs4好用多了，记住一点，尽可能地匹配，.*?表示匹配所有字符，(.*?)表示将匹配到的字符存下来
    iterms = re.findall(pattern1, content)
    for iterm in iterms:
        if iterm[1] not in stock_dict.keys():
            stock_dict[iterm[1]]=[]
        stock_dict[iterm[1]].append(iterm[0])
        if iterm[0] in date:
            all_stock.append(iterm[1])

#使用字典统计列表词频
all_stock_name_count_dict = dict.fromkeys(all_stock, 0)
for i in all_stock:
    all_stock_name_count_dict[i] +=1

#对字典按value排序
final_result=sorted(all_stock_name_count_dict.items(),key=lambda item:item[1],reverse=True)
for i in final_result:
    print(i[0]+':'+str(i[1]),file=open('1.txt','a'))
    for j in stock_dict[i[0]]:
        print(j,file=open('1.txt','a'))


