import json
import requests
import pandas as pd
import datetime
import numpy as np 
import os 


url = 'https://www.alphavantage.co/query?'

def get_dates_and_close_df(resp_json, symbol, save_df=False):
    try:
        print(resp_json, type(resp_json))
        assert len(resp_json)!=0, f"response JSON is null for given symbol {symbol}"
        df = pd.DataFrame.from_dict(resp_json["Time Series (Daily)"], orient='index').rename_axis(index='dates')
        df.drop(labels=["3. low", "2. high", "1. open", "5. volume" ], axis='columns', inplace=True)
        df.rename(columns={"4. close" : "price"}, inplace=True)
        df.reset_index(inplace=True)
        df["price"] = df["price"].astype(float)
        df["dates"] = pd.to_datetime(df["dates"])
        if save_df:
            print(df.to_excel(os.path.join("last_100_days", symbol+".xlsx")))
    except KeyError:
        print(f"RESPONSE JSON FOR SYMBOL {symbol}\n{resp_json}")
    return df

def get_last_100_days(symbol):
    params = {"function":"TIME_SERIES_DAILY",
    "symbol": symbol,
    "outputsize":"compact",
    "apikey" : "N1MQS1YA919A1VSN",
    }
    headers = {}
    resp = requests.get(url = url, params = params, headers = headers)
    # return resp.json()
    return get_dates_and_close_df(resp.json(), symbol, save_df=True)

def get_last_20_years(symbol):
    params = {"function":"TIME_SERIES_DAILY",
    "symbol": symbol,
    "outputsize":"full",
    "apikey" : "N1MQS1YA919A1VSN",
    }
    headers = {}
    resp = requests.get(url = url, params = params, headers = headers)
    return get_dates_and_close_df(resp.json(), symbol)

def get_avg_last_20weeks(xdf, symbol):
    week_averages = {
    'week_count':[],
    'start_date':[],
    'average':[]
    }    
    week_count = 20
    try:
        for i in range(0,len(xdf),5):
            avg = np.mean(xdf.loc[i:i+4]['price'])
            week_averages['average'].append(avg)
            week_averages['week_count'].append(week_count)
            week_averages['start_date'].append(xdf.loc[i]['dates'])
            # week_averages['start_date'].append(str(xdf.loc[i]['dates']))
            week_count -= 1
    except Exception as err:
        print(f"Error at {i} - {err}")
    week_averages = pd.DataFrame(week_averages)
    week_averages.to_excel(os.path.join("last_20_week_mean", symbol+".xlsx" ))
    return week_averages


symbol_token = "ASHOKLEY.BSE"

xdf = get_last_100_days(symbol_token)


