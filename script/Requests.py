import requests
from urllib.parse import urlsplit


class Requests:
    def __init__(self):
        pass

    def requests(self, urls):
        try:
            req = requests.get(urls)
            status_code = req.status_code
            url = urlsplit(urls).path
            return status_code, url
        except:
            pass