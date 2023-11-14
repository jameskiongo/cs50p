import json
import requests
import sys
# cli must be there
# if len(sys.argv) != 2:
#     sys.exit("Missing command-line argument")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = response.json()
for result in o["bpi"]:
    print(result[1][2])
# print(response)
# be in float
# output bitcoin in usd using , as a thousands separator