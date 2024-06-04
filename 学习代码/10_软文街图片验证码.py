import requests
import ddddocr

res = requests.post(
    url="https://api.ruanwen.la/api/auth/captcha/generate"
)
res=res.json()
captcha_token = res["data"]["captcha_token"]
src = res["data"]["src"]
# print(captcha_token)
# print(src)
res_image = requests.get(url=src)
# print(res_image.content)
ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res_image.content)
print(code)

res_login = requests.post(
    url="https://api.ruanwen.la/api/auth/authenticate",
    data=
    {
        "mobile":"18555962537",
        "device":"pc",
        "password":"123456",
        "captcha_token":captcha_token,
        "captcha":str(code),
        "identity":"advertiser"
    }
)
print(res_login.text)