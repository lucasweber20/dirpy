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
            if sc:
                if "," in sc:
                    for check_sc in sc.split(','):
                        if str(status_code) == check_sc:
                            return status_code, url
                else:
                    if str(status_code) == sc:
                        return status_code, url
            else:
                return status_code, url
        except:
            pass