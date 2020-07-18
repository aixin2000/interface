"""
    获取token值
"""

# 导包 unittest api_token
import unittest
from api.api_token import ApiToken
from parameterized import parameterized
# from data import data_token
from tools.read_json import ReadJson
# 读取数据函数
def get_data():
    datas = ReadJson("token_more.json").read_json()
    # 新建空列表，添加读取json数据
    list1 = []
    for data in datas.values():
        list1.append((data.get("url"),
                      data.get("grant_type"),
                      data.get("appid"),
                      data.get("secret"),
                      data.get("expires_in")))
    return list1
# 新建测试类
class Test_Toekn(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_token(self, url, grant_type, appid, secret, expires_in):
        """
            输入正确的参数是否能够获取token值。
        """
        # url = "https://api.weixin.qq.com/cgi-bin/token"
        # grant_type = data_token.data1["grant_type"]
        # appid = data_token.data1["appid"]
        # secret = data_token.data1["secret"]
        a = ApiToken()
        r = api_get_token(url, grant_type, appid, secret)
        print(r.text)
        self.assertEqual(expires_in, r.json()['expires_in'])
        # self.assertEqual(200, r.status_code)


if __name__ == '__main__':
    unittest.main()

# 新建测试方法

# 暂时存放数据 url，grant_type，appid，secret

# 调用登录方法

# 断言 响应信息 及 状态码
