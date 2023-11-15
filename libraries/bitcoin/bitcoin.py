import json
import requests
import sys
# cli must be there
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
while True:
    try:
        number = float(sys.argv[1])
        break
    except:
        sys.exit("Command-line argument is not a number")

while True:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        bitcoin = o["bpi"]["USD"]["rate_float"]
        total = number * bitcoin
        print(f"${total:,.4f}")
        break
    except requests.RequestException:
        ...
    

# print(response)
# be in float
# output bitcoin in usd using , as a thousands separator