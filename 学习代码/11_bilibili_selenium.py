import time
# https://googlechromelabs.github.io/chrome-for-testing/#stable 谷歌驱动
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
service = Service("driver/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service = service)

#全局配置
# driver.implicitly_wait(10)

driver.get("https://passport.bilibili.com/login")
#
# sms_btn = driver.find_element(
#     By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'
# )
def func(dv):
    return  dv.find_element( By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]')


sms_btn = WebDriverWait(driver,30,0.5).until(func)

sms_btn.click()
time.sleep(1)
driver.execute_script('document.querySelector(".area-code-select").children[1].click()')
username = driver.find_element(
    By.XPATH,'//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input'
)
time.sleep(1)
username.send_keys("18555962537")
cookies_list = driver.get_cookies()
print(cookies_list)

time.sleep(10)
driver.close()
