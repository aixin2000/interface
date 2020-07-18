import unittest
from api.api_delete import api_post_delete
from parameterized import parameterized
from tools.read_json import ReadJson


def get_data():
    data = ReadJson("delete.json").read_json()
    list1 = []
    list1.append((data.get("url"),
                  data.get("number"),
                  data.get("errcode")))
    return list1


class Test_Delete(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_delete(self, url, number, errcode):
        r = api_post_delete(url, number)
        print(r.json())
        self.assertEqual(errcode, r.json()['errcode'])


if __name__ == '__main__':
    unittest.main()
