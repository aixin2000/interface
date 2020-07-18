import unittest
from api.api_obtain import ApiObtain
from tools.read_json import ReadJson
from parameterized import parameterized


def get_data():
    data = ReadJson("obtain.json").read_json()
    list1 = []
    list1.append((data.get("url"),
                  data.get("token"),
                  data.get("status_code")))
    return list1


class Test_Obtain(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_obtain(self, url, token, status_code):
        # url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        # token = "31_dTuQaAHW6uSLNeGj2tSZoqjTMdMAfHG3oUQaqw4mbrjbTYKzUcpoJJupzfpsHrsJ6bKpkKfYdxQVtvboL6YfZQuXpY2H6oUZslnzG6329-B3K7zRJzHbzbTHDEsAJ8CVmaLrun_atcSj9a14LZUeABAFTO"
        r = ApiObtain().api_get_obtain(url, token)
        print(r.json())
        self.assertEqual(status_code, r.status_code)


if __name__ == '__main__':
    unittest.main()
