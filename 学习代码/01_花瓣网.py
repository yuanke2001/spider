import requests
import json
res =requests.get(
    url="https://api.huaban.com/boards/13919785/pins?limit=40&max=5603886670&fields=pins:PIN,board:BOARD_DETAIL,check"
)
# 响应内容转化为字符串形式
# print(res.text)
# 转化为json字典格式
res_dict=json.loads(res.text)
res_pin =res_dict["pins"]
print(res_pin)
for i in res_pin:
    print(i['like_count'])