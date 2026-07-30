import concurrent.futures
import argparse
import time
from script.Parser import Parser
from script.Requests import Requests


parser = argparse.ArgumentParser()

args = parser.add_argument("-u", "--url", help='Set url, example: -u https://example.com/', type=str)
args = parser.add_argument("-w", "--wordlist", help="Specify file with values, example: -o directories.txt", type=str)
args = parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 5", default=1, type=int)
args = parser.add_argument("-sc", "--status_code", help="Specify status code, example: -sc 200 or -sc 200,301", type=str)
args = parser.add_argument("-x", "--extension", help="Specify extension, example: -x .php or -x .php,.js", type=str)
args = parser.add_argument("-to", "--timeout", help="Specify timeout in requests, example: --timeout 10", default=5, type=int)
args = parser.add_argument("-d", "--delay", help="Specify delay in requests, example: --delay 5", type=int)
args = parser.add_argument("-o", "--output", help="Specify output file, example: -o outputs.txt", type=str)

args = parser.parse_args()

def main():
    # Flags
    url = args.url
    wordlist = args.wordlist
    status_code = args.status_code
    extension = args.extension
    threads = args.thread
    output = args.output
    timeout = args.timeout
    delay = args.delay

    # Parser url
    parser = Parser(url, wordlist)
    urls_parsed = parser.parser()

    # Requests
    requests = Requests()
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(requests.requests, url, status_code, timeout) for url in urls_parsed]
        for future in concurrent.futures.as_completed(futures):
            status_code_result = future.result()
            if delay:
                time.sleep(delay)
            if status_code_result:
                if status_code_result[0] >= 200 and status_code_result[0] < 300:
                    print(f"{status_code_result[1]} -> \033[92m{status_code_result[0]}\033[00m")
                elif status_code_result[0] >= 300 and status_code_result[0] < 400:
                    print(f"{status_code_result[1]} -> \033[36m{status_code_result[0]}\033[00m")
                elif status_code_result[0] >= 400 and status_code_result[0] < 500:
                    print(f"{status_code_result[1]} -> \033[33m{status_code_result[0]}\033[00m")
                elif status_code_result[0] >= 500 and status_code_result[0] < 600:
                    print(f"{status_code_result[1]} -> \033[31m{status_code_result[0]}\033[00m")
                if output:
                    write_file = open(output, "a").write(f"{status_code_result[1]} -> {status_code_result[0]}\n")
            else:
                continue

if __name__ == "__main__":
    main()