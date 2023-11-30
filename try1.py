import pandas as pd
import os

# Assuming you have a DataFrame named 'df' with 'dates' and 'price' columns
# Sample data
def analyse_latest_price(symbol):
    df = pd.read_excel(os.path.join("last_100_days", f"{symbol}.xlsx"))

    # Convert 'dates' column to datetime format
    df['dates'] = pd.to_datetime(df['dates'])

    # Sort the DataFrame by date in descending order
    df = df.sort_values(by='dates', ascending=False)

    # Assuming latest_price is the latest price for which you want to find a close match
    latest_price = df.iloc[0]["price"] + 1  # Replace this with your actual latest price
    latest_date = df.iloc[0]['dates']

    # Set a threshold for the price difference
    price_threshold = 1.0  # Adjust this threshold based on your requirement

    # Find the closest match
    closest_match = df.loc[(df['price'] - latest_price).abs() < price_threshold]

    if not closest_match.empty:
        closest_date = closest_match.iloc[0]['dates']
        closest_price = closest_match.iloc[0]['price']
        print(f"The closest match to {latest_price} ({latest_date}) is on {closest_date} with a price of {closest_price}")
    else:
        print(f"No close match found for {latest_price}")

analyse_latest_price("ASHOKLEY.BSE")

