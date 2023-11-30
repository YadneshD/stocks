import json
import requests

# INTRA-DAY
# params = {"function":"TIME_SERIES_INTRADAY",
# "symbol":"IBM",
# "interval" : "1min",
# "apikey" : "N1MQS1YA919A1VSN",
# }

## DAILY
params = {"function":"TIME_SERIES_DAILY",
"symbol":"ASHOKLEY.BSE",
"outputsize":"compact",
"apikey" : "N1MQS1YA919A1VSN",
}

# params = {"function":"SYMBOL_SEARCH",
# "keywords":"ASH.BSE",
# "apikey" : "N1MQS1YA919A1VSN",
# }

url = 'https://www.alphavantage.co/query?'

headers = {}

x = requests.get(url = url, params = params, headers = headers)

print(x.text)