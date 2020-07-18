import unittest
from api.api_create import ApiCreate
from tools.read_json import ReadJson
from parameterized import parameterized

def get_data():
    data = ReadJson("create.json").read_json()
    list1 = []
    list1.append((data.get("url"),
                  data.get("city"),
                  data.get("lable")))
    return list1
class Test_Create(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_create(self, url, city, lable):
        # url = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token=31_dTuQaAHW6uSLNeGj2tSZoqjTMdMAfHG3oUQaqw4mbrjbTYKzUcpoJJupzfpsHrsJ6bKpkKfYdxQVtvboL6YfZQuXpY2H6oUZslnzG6329-B3K7zRJzHbzbTHDEsAJ8CVmaLrun_atcSj9a14LZUeABAFTO"
        # city = "eqweq"
        r = ApiCreate().api_post_create(url, city)
        print(r.json())
        self.assertEqual(lable, r.json()["tag"]["id"])


if __name__ == '__main__':
    unittest.main()
