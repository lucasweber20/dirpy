import requests
from urllib.parse import urlsplit


class Requests:
    def __init__(self):
        pass
    
    def requests(self, urls, sc):
        try:
            req = requests.get(urls)
            status_code = req.status_code
            url = urlsplit(urls).path
            if sc != 1:
                if status_code == sc:
                    return status_code, url
                else:
                    pass
            else:
                return status_code, url
        except:
            pass