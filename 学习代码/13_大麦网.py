import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# # 提取代理API接口，获取1个代理IP
# api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=o6snh2wsb6rjhj8upk9v&signature=foua9b0qhj2n24dwp2jzdk3sei30gf5x&num=1&pt=1&sep=1"
#
# # 获取API接口返回的代理IP
# proxy_ip = requests.get(api_url).text
#
# # 用户名密码认证(私密代理/独享代理)
# username = "d1663723300"
# password = "9hfy5ukb"
# proxies = {
#     "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
#     "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
# }

# 白名单方式（需提前设置白名单）
# proxies = {
#     "http": "http://%(proxy)s/" % {"proxy": proxy_ip},
#     "https": "http://%(proxy)s/" % {"proxy": proxy_ip}
# }

#加载谷歌驱动
service = Service("driver/chromedriver-win64/chromedriver.exe")

opt =  webdriver.ChromeOptions()
# 无界面模式
# opt.add_argument('headless')
#禁止加载页面图片
opt.add_argument('blink-setting=imagesEnabled=false')
opt.add_argument('disable-infobars')  # 禁用inforbar，无效
# 关闭'Chrome目前受到自动测试软件'的提示
opt.add_experimental_option('useAutomationExtension', False)
opt.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(service = service,options = opt)
driver.implicitly_wait(10) #隐式等待10秒

#加载隐藏文件
with open('hide.js') as f:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": f.read()})



# 使用代理IP发送请求
# 1.打开大麦网
driver.get('https://www.damai.cn/')

# 2.搜索框+输入
tag = driver.find_element(
    By.XPATH,
    '//input[@class="input-search"]'
)
tag.send_keys("周杰伦")

# 3.点击搜索
tag = driver.find_element(
    By.XPATH,
    '//div[@class="btn-search"]'
)
tag.click()

# 4.查询列表
tag_list = driver.find_elements(
    By.XPATH,
    '//div[@class="search__itemlist"]//div[@class="items"]'
)
for tag in tag_list:
    title = tag.find_element(By.XPATH, 'div[@class="items__txt"]/div[1]/a').text
    print(title)


time.sleep(2000)
driver.close()
