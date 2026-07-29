import argparse


parser = argparse.ArgumentParser()

args = parser.add_argument("-u", "--url", help='Set url, example: -u https://example.com/', type=str)
args = parser.add_argument("-w", "--wordlist", help="Specify file with values, example: -o directories.txt", type=str)
args = parser.add_argument("-o", "--output", help="Specify output file, example: -o outputs.txt", type=str)
args = parser.add_argument("-t", "--thread", help="Specify threads number, example: -t 3", type=int)

args = parser.parse_args()

def main():
    pass

if __name__ == "__main__":
    main()