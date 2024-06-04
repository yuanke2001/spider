import requests
from bs4 import BeautifulSoup

res =requests.get(
    url="https://car.yiche.com/"
)

soup = BeautifulSoup(res.text ,features="html.parser")

tag_list = soup.findAll(name="div",attrs={"class":"item-brand"})

for tag in tag_list:
    print(tag.attrs["data-name"])





