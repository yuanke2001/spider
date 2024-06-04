import requests
import json

res=requests.get(
    url="https://v26-web.douyinvod.com/9de20b1bfb9309ad531037943ec68710/65d6153f/video/tos/cn/tos-cn-ve-15c001-alinc2/okEzy0QGVb6oABMCSpIA4BYAh6DxluvIIgNfeB/?a=6383&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=1219&bt=1219&cs=0&ds=6&ft=bvTKJbQQqUCIf_EZFo0OqY8hFgpi5_BuejKJRjkC0.0P3-I&mime_type=video_mp4&qs=1&rc=Zmc6ZTk4ZTc8NzozaTc1aEBpM2hmNTk6ZndqcDMzNGkzM0BhMC01YmMuNTMxMGMzYC4tYSMzMDAucjQwNWZgLS1kLTBzcw%3D%3D&btag=e00030000&dy_q=1708525041&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20240221221721F2331811D103AA1C0A75"

)

with open("ceshi.mp4",mode="wb") as f:
    f.write(res.content)