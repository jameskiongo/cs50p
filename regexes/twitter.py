import re

url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)twitter\.com/", "", url)
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$", url, re.IGNORECASE):
    print(f"username: ", matches.group(1))