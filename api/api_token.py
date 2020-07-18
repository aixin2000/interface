# 导包
import requests

# 新建类
def api_get_token(url, grant_type, appid, secret):
    data = {"grant_type": grant_type, "appid": appid,
            "secret": secret}
    return requests.get(url=url, params=data)


class ApiToken:
    # 新建方法
    pass

"""
    提示：
        url,grant_type,appid,secret:最后都需要从data数据文件中读取出来，所以我们这里使用动态传参。
"""
