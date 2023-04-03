import requests
import time
import winsound

addresses_file = "eaddresses.txt"
api_key = "Enter API KEY HERE"
api_url = "https://api.etherscan.io/api"

def check_balance(address):
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": api_key
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    balance = float(data["result"]) / (10 ** 18)
    print(f"Balance for address {address}: {balance} ETH")
    if balance > 0:
        winsound.Beep(1000, 1000)
    if balance > 0:
        with open("balance-found.txt", "a") as f:
            f.write(f"{address}: {balance} ETH\n")

with open(addresses_file) as f:
    addresses = f.read().splitlines()

 # write the balance to the found.txt file if it's positive
    

for address in addresses:
    check_balance(address)
    time.sleep(1)
