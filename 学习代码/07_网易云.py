from bs4 import BeautifulSoup
import requests

res = requests.get(
    url="https://music.163.com/discover/playlist/?cat=%E5%8D%8E%E8%AF%AD",
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Referer":"https://music.163.com/"
    }
)

soup=BeautifulSoup(res.text , features="html.parser")

ul=soup.find(name="ul" , attrs={"class":"m-cvrlst f-cb","id":"m-pl-container"})

for child in ul.findAll(recursive=False):
    title = child.find(name="a",attrs={"class":"tit f-thide s-fc0"}).text
    img_url = child.find(name="img").attrs['src']
    print(title,img_url)
    # 下载图片
    # img_res = requests.get(url=img_url)
    # img = title.split()[0]+".jpg"
    # with open(img , mode="wb") as f:
    #     f.write(img_res.content)