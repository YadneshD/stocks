import requests

url = "https://api-v2.upstox.com/market-quote/ohlc?symbol=FLUOROCHEM"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)