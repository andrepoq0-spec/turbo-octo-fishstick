
PRIVATE_KEY="48bd6407623ab26eb2581c95a7be836b2ba9937f1c217b1b06a127be3c85e43a"
MNEMONIC="SKI ROOF MOON HEART THROW ART EMOTION EXILE HOLD DANGER LINK MARGIN"
ADDRESS="TYYBTFixT53TvGYiMXt4GcuWrwJpjK3tTF"

import requests

wallet_address = ADDRESS

url = f"https://blockchair.com{wallet_address}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    balance_sat = data["data"][wallet_address]["address"]["balance"]
    balance_btc = balance_sat / 100000000
    print(f"{balance_btc} BTC")
else:
    print("error")
