import requests
from urllib.parse import urlsplit


class Requests:
    def __init__(self):
        pass
    
    def requests(self, urls, sc, timeout):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"}
        try:
            req = requests.get(urls, headers=headers, allow_redirects=False, timeout=timeout)
            status_code = req.status_code
            url = urlsplit(urls).path
            length = len(req.content)
            if sc:
                if "," in sc:
                    for check_sc in sc.split(','):
                        if str(status_code) == check_sc:
                            return status_code, url, length
                else:
                    if str(status_code) == sc:
                        return status_code, url, length
            else:
                return status_code, url, length
        except:
            pass