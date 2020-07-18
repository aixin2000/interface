import requests

class ApiObtain():
    def api_get_obtain(self, url, token):
        data = {"access_token": token}
        return requests.get(url=url, params=data)