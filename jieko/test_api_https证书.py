import requests

url_xie = "https://www.ctrip.com/"
# 发送请求时候忽略证书，证书的参数verify
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)# 警告行消失
r = requests.get(url=url_xie, verify=False)# verify的默认参数师true，值为false表示忽略证书。
print(r.text)

# 在verify里面添加证书
r = requests.get(url=url_xie, verify="证书路径")# verify的默认参数师true，值为false表示忽略证书。
print(r.text)