import requests

url = "http://106.12.126.197:3000/"

r = requests.get(url=url,auth=('cxy001','123456'))
print(r.text)

