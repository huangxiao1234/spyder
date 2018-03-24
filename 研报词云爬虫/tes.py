import requests
import re
from  wordcloud import WordCloud
from matplotlib import pyplot as plt
headers = {'X-Requested-With': 'XMLHttpRequest',
           'Referer': 'http://xueqiu.com/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
           'Host': 'xueqiu.com',
           #'Connection':'keep-alive',
           #'Accept':'*/*',
           'cookie':'device_id=4d45cb91deea3586d9504778e5623ecf; s=g9122owmy0; __utmz=1.1519631773.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=1.190366839.1519631773.1519631773.1519664565.2; __utmt=1; __utmb=1.1.10.1519664565; aliyungf_tc=AQAAACrn7EiGMgEAadleZbKZM/NZpput; xq_a_token=5c915d14d91dc74b5f2e4c3b4753137ae66c1926; xq_a_token.sig=CGCHkBovlWaQtWbwukG6L3FRNIA; xq_r_token=e796a61232e2cf0d90d560d30af22b227d8f7eeb; xq_r_token.sig=VeCkcFeNm3Vszkg9DbEZW9Pg0pA; u=951519664856314; Hm_lvt_1db88642e346389874251b5a1eded6e3=1519631051,1519664857; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1519664857'
           '__utmc=1; __utmz=1.1433017807.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1433017809; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1433017809'}

cont=requests.get('https://xueqiu.com/stock/rank.json?size=8&_type=12&type=12',headers=headers).text
p=re.compile('"name":"(.*?)"',re.S)
iterms=re.findall(p,cont)
print(iterms)
# wl_space_split = " ".join(iterms)
#
# # 对分词后的文本生成词云
# my_wordcloud = WordCloud().generate(wl_space_split)
#
# # 显示词云图
# plt.imshow(my_wordcloud)
# # 是否显示x轴、y轴下标
# plt.axis("off")
# plt.show()