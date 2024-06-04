import  requests
import time
import hashlib
import re
from bs4  import  BeautifulSoup
res_1= requests.get(
    url="https://bbs.pku.edu.cn/v2/home.php",
    headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Referer":"https://cn.bing.com/"
    }
)
cookie_dict = res_1.cookies.get_dict()
# var r = BDWM.getGlobalTimestamp()
# , s = CryptoJS.MD5(i + n + r + i).toString().toLowerCase();

# window.BDWM.getGlobalTimestamp = function() {
#         return window.globalTime ? Math.floor(Date.now() / 1e3) - window.localTime + window.globalTime : Math.floor(Date.now() / 1e3)
#     }

 # 根据实际情况设置 window.localTime 的值 # 根据实际情况设置 window.globalTime 的值
res=requests.get(
    url="https://bbs.pku.edu.cn/v2/home.php"
)

pattern = r'id="global-time">([^<]+)</div>'
match = re.search(pattern, res.text)
if match:
    extracted_text = match.group(1)
    # print(extracted_text)
else:
    print("No match found")

current_time = int(time.time())
global_time=int(extracted_text)
local_time = global_time+1
r = (
    current_time - local_time + global_time
)

i = "asd" #password
n="zhangkai"   #username
data_string= i + n + str(r) + i

obj = hashlib.md5()
obj.update(data_string.encode("utf-8"))
md5_string = obj.hexdigest()
# print(r)
# print(md5_string)
# print(cookie_dict)
print(current_time)
res = requests.post(
    url="https://bbs.pku.edu.cn/v2/ajax/login.php",
    data={
        "username":n,
        "password":i,
        "keepalive":"0",
        "time":str(current_time),
        "t":str(md5_string)
    },
    headers={
    "Cookie":"skey=82be1984d4a292f8; uid=15265",
    "Referer":"https://bbs.pku.edu.cn/v2/home.php",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
    }
    # cookies=cookie_dict
)

print(res.text)
