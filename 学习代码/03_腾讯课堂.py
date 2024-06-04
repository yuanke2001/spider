import requests
import json

res =requests.post(
    url="https://ke.qq.com/cgi-proxy/course_list/search_course_list?bkn=&r=0.0075",
    #如果resquest payload是字典型使用json，如果是form表单格式，使用data
    headers ={
    #referer是关键，代表访问的前一页面
    "Referer":"https://ke.qq.com/course/list?mt=1001&st=2004&quicklink=1&page=1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    } ,
   json = {"mt":"1001","st":"2004","page":"1","visitor_id":"7549940295934665","finger_id":"572ae2487883fa634a3db791b032c6bc","platform":3,"source":"search","count":24,"need_filter_contact_labels":1}
)
res_dict=json.loads(res.text)
res_result=res_dict["result"]["search_result"]
for i in res_result:
    print(i["course"]["name"])
