import requests


class Requests:
    def __init__(self):
        pass

    def requests(self, urls):
        try:
            req = requests.get(urls)
            status_code = req.status_code
            url = req.url
            return status_code, url
        except:
            pass