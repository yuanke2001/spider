import requests
from bs4 import BeautifulSoup

res = requests.post(
    url="https://passport.china.com/logon",
    data={
        "userName":"18555962537",
        "password":"qwe123456"
    },
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Referer":"https://passport.china.com/logon",
    "X-Requested-With":"XMLHttpRequest"
    }
)
cookie_dict = res.cookies.get_dict()
# print(res.text)
# print(cookie_dict)

# cookie_dict ={'nickname': 'china_3735rrkz16791043', 'lastlogindate': '2024-03-05', 'lastlogintime': '"20:58:57"', 'lastloginip': '112.31.21.129', 'bindMobile': '"1@185*****537"', 'CHINACOMID': '47ed8077-aa4a-4b43-9f70-7315876543259', 'CP_USER': 'FKBo6w-aaDHw25s42C49hm4cSEUTXTzbzIpsuaQNIsL70GDULkM7ajxMW8jARO4t-JQ7h0wOBu1OfUfL7ob291a%2FMskV84bFfJDwJ-fZurTp6jej2klaldLTo57ixlYRuED4JxwmYz0KpEgsBxvuYg-86VP2FwRU7UTvv95iR4r6XGL3MGmm%2FWOWDbTa83o4oyBlp0qUbvQLXG0S4O6yaCxM3d9zMH5Wkvviu%2FJ4kJsiC44IuLq2ow%3D%3D', 'CP_USERINFO': '4Gkk4uas%2FGU6V4cAn8Kr14YtZHaRsQ3bb0iKxhYvuaLYLT-rPEFbvbaQzjvqSKm2v8Fd1lQ14weg0PM1aAxGqjzFStaNWwdXEhS3Zzs0jusNqPIZSkWIUHBpa7NyrsBUv2O8QVvh3O4yqW9wAjnfpw%3D%3D', 'china_variable': 'jpEe7N32pYz8SAjCjL8fnh2eLZiI1D/EC6dYmS6/lLUOPrHJGj-IxLIHbACvhNcaC9z3Z8pi2hy0JtYoQGGXmsutg32di8lhAZaSKKJ8BFBt-lJZl7B3R-LY1hWhKpza', 'SESSION_COOKIE': '46'}
res =requests.get(
    url="https://passport.china.com/main",
    cookies = cookie_dict
)
print(res.text)

soup =BeautifulSoup(res.text , features="html.parse")
tag = soup.find(attrs={"id":"usernick"})
# tag = soup.find(attrs={"id":"usernick"})
print(tag.text)
# print(tag.attrs["title"])
