import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    src = re.search(r'src="([^"]*)"', s)
    if src:
        src_link = src.group(1)
        if match := re.search(r'^https?://(?:www\.)?youtube\.com/(?:embed/)?([a-zA-Z0-9_]+)$', src_link, re.IGNORECASE):
            share =  match.group(1)
            link = "https://youtu.be/"
            return f"{link}{share}"


if __name__ == "__main__":
    main()