import requests


class Requests:
    def __init__(self):
        pass

    def requests(self, url):
        try:
            req = requests.get(url).status_code
            return req
        except:
            pass