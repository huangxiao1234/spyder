import requests
import re
import datetime
from tqdm import tqdm
from wordcloud import WordCloud
from matplotlib import pyplot as plt
"""
静态爬取慧博
"""
now_time = datetime.datetime.now()
date=[]
endday=60
for i in range(1,endday):
    yes_time = now_time + datetime.timedelta(days=-(endday-1)+i)
    date.append(yes_time.strftime('%m-%d'))

stock_date_and_name={}
all_stock_name=[]
for i in range(len(date)):
    stock_date_and_name[date[i]]=[]
for i in tqdm(range(1,100)):
    url = "http://hibor.net/microns_1_"+str(i)+".html"
    content= requests.get(url).text

    pattern1=re.compile('<td>.*?<span class="tab_lta"><a href=".*?" target="_blank">(.*?)</a>.*?</td>',re.S)
    iterms=re.findall(pattern1,content)
    for iterm in iterms:
        temp=iterm.split('-')
        date_now=temp[4][2]+temp[4][3]+'-'+temp[4][4]+temp[4][5]
        if date_now in stock_date_and_name.keys():
            stock_date_and_name[date_now].append(temp[1])
            all_stock_name.append(temp[1])

all_stock_name_count_dict = dict.fromkeys(all_stock_name, 0)
for i in all_stock_name:
    all_stock_name_count_dict[i] +=1

stock_wordcloud=[]
final_result=sorted(all_stock_name_count_dict.items(),key=lambda item:item[1],reverse=True)
for i in final_result[0:24]:
    stock_wordcloud.append(i[0])
    print('{'+'name:'+i[0]+','+'value:'+str(i[1])+'}')

# wl_space_split = " ".join(stock_wordcloud)
#
# # 对分词后的文本生成词云
# my_wordcloud = WordCloud().generate(wl_space_split)
#
# # 显示词云图
# plt.imshow(my_wordcloud)
# # 是否显示x轴、y轴下标
# plt.axis("off")
# plt.show()