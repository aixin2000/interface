import requests

class ApiCreate():
    def api_post_create(self, url, city):
        data = {"tag": {"name": city}}
        return requests.post(url, json=data)
