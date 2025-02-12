import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
from datetime import datetime

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,  
    "page": 1,
    "sparkline": False
}

def fetch_crypto_data():
    """Fetch live crypto data and return a DataFrame"""
    try:
        response = requests.get(API_URL, params=PARAMS)
        data = response.json()

        if not isinstance(data, list):  # Ensure response is a list of crypto data
            print("Unexpected API response:", data)
            return None  

        df = pd.DataFrame(data)
        print("Fetched Columns:", df.columns.tolist())  # Debugging line

        expected_cols = {"name", "current_price", "market_cap", "price_change_percentage_24h"}
        actual_cols = set(df.columns)

        if not expected_cols.issubset(actual_cols):
            print(f"Missing columns: {expected_cols - actual_cols}")
            return None  

        return df[["name", "current_price", "market_cap", "price_change_percentage_24h"]]
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def plot_live_data():
    """Fetch live data and plot top 5 cryptos by market cap"""
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))
    last_update_time = "Waiting for first update..."

    while True:
        df = fetch_crypto_data()
        if df is not None and not df.empty:
            top5 = df.nlargest(5, "market_cap")

            ax.clear()
            ax.bar(top5["name"], top5["current_price"], color="skyblue")
            ax.set_ylabel("Current Price (USD)")
            ax.set_xlabel("Cryptocurrency")
            ax.set_title("Top 5 Cryptocurrencies by Market Cap")

            last_update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ax.text(0.5, 0.95, f"Last Update: {last_update_time}", ha="center", va="center", 
                transform=ax.transAxes, fontsize=10, color="red")
        
        plt.draw()
        plt.pause(300)  # 5 minutes

if __name__ == "__main__":
    plot_live_data()
