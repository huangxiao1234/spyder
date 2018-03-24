
import requests
import re
import datetime

import sys
from tqdm import tqdm
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
for i in tqdm(range(1,30)):

    browser.get("http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0" + str('x'))
    element=browser.find_element_by_id("gopage")
    element.clear()
    element.send_keys(str(i))
    print(i)
    e=browser.find_element_by_xpath('//a[@class="btn_link"]')
    e.click()
    handles = browser.window_handles
    browser.switch_to.window(handles[0])
    time.sleep(5)
    content = browser.page_source
    browser.close()
    pattern1 = re.compile(
        'class="txt">(.*?)</span></td><td><a href=".*?" class="hqPopCls" data_code=".*?" data_name="(.*?)"', re.S)
    iterms = re.findall(pattern1, content)

    print(iterms)


