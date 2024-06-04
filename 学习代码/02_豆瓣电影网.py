import  json
import requests

res = requests.get(
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0",
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }
)

# print(res.text)

res_dict=json.loads(res.text)
res_sub=res_dict["subjects"]
for i in res_sub:
    print(i['title']+" "+i['rate'])