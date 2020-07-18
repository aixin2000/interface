import requests
import json

# 获取token值
wx_url = " https://api.weixin.qq.com/cgi-bin/token"
token_data = {"grant_type": "client_credential", "appid": "wxa08749913379550d",
              "secret": "12172e3254a4bf79d383b50109f6137c"}
s = requests.session()
token_req = s.get(wx_url, params=token_data)
print(token_req.text)
# wx_token = token_req.json()['access_token']

# 创建标签
# create_url = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token=30_AyTP09ZcSAfgxGu-fpPoXM0R--ej5rlzfLiHccV8xRR-mcDOKblE6gXYYfvY5uHLN5XddtU-vnM9g_vBkMAP5GEMwHNq4oUIlowqbBXLPGCC7-KL2ZcYXIs0jR4iJCaBmFvFYs4Xd5LvLfJqMGFaAIAWQP"
# create_json = {"tag": {"name": "广东t3933"}}
# create_data = {"access_token": wx_token}
# create_req = requests.post(url=create_url, data=json.dumps(create_data), json=create_json)
# create_req = s.post(url=create_url, json=create_json)
# print(create_req.json())
# print(create_req.content.decode('unicode_escape'))
# print(create_req.text.encode('utf-8').decode('unicode_escape'))


# 获取标签
# curr_url = "https://api.weixin.qq.com/cgi-bin/tags/get"
# curr_data = {"access_token": wx_token}
# curr_req = requests.get(curr_url, params=curr_data)
# print(curr_req.text)

# 删除标签
# url = "https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=30_AyTP09ZcSAfgxGu-fpPoXM0R--ej5rlzfLiHccV8xRR-mcDOKblE6gXYYfvY5uHLN5XddtU-vnM9g_vBkMAP5GEMwHNq4oUIlowqbBXLPGCC7-KL2ZcYXIs0jR4iJCaBmFvFYs4Xd5LvLfJqMGFaAIAWQP"
# delete_json = {"tag": {"id": 124}}
# r = requests.post(url=url, json=delete_json)
# print(r.text)



