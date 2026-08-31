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
