from selenium import webdriver
# 进入浏览器设置
browser = webdriver.Chrome()
url = "https://xueqiu.com/stock/rank.json?size=8&_type=12&type=12"
browser.get(url)
print(browser.page_source)



