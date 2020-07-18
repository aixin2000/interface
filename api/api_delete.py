import requests


def api_post_delete(url, number):
    data = {"tag": {"id": number}}
    return requests.post(url=url, json=data)



