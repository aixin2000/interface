# 导包
import json

# 打开json文件并获取文件流
class ReadJson():
    # 调用load方法加载文件流
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == '__main__':
    datas = ReadJson("token_more.json").read_json()
    # 新建空列表，添加读取json数据
    list1 = []
    # 使用遍历
    for data in datas.keys():
        list1.append((data.get("url"),
                  data.get("grant_type"),
                  data.get("appid"),
                  data.get("secret"),
                  data.get("expires_in")))
    print(list1)

