from urllib.parse import urlsplit


class Parser:
    def __init__(self, url, wordlist):
        self.url = url
        self.wordlist = wordlist

    def parser(self):
        parsed_urls = []
        scheme = urlsplit(self.url).scheme
        hostname = urlsplit(self.url).netloc
        path = urlsplit(self.url).path
        read_wordlist = open(self.wordlist, encoding='utf-8').read().splitlines()
        for word in read_wordlist:
            if path:
                parser_url = f"{scheme}://{hostname}{path}{word}"
            else:
                parser_url = f"{scheme}://{hostname}/{word}"
            parsed_urls.append(parser_url)
        return parsed_urls

    def parser_extension(self, ext):
        parsed_urls = []
        urls = self.parser()
        for url in urls:
            if "," in ext:
                for extension in ext.split(','):
                    parser_urls = url+extension
                    parsed_urls.append(parser_urls)
            else:
                parser_urls = url+ext
                parsed_urls.append(parser_urls)
        return parsed_urls