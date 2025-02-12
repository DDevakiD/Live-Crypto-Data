import requests
import pandas as pd
import xlwings as xw
import time
import datetime

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 1,
    "sparkline": False
}

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list):
            df = pd.DataFrame(data)
            return df[["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]
    return None  # Return None if request fails or data is missing

def update_excel():
    wb = xw.Book("CoinGecko111.xlsx")  # Open or create Excel file
    sheet = wb.sheets["Sheet1"]
    wb.app.screen_updating = True  # Prevent freezing

    while True:
        start_time = time.time()  # Track start time

        df = fetch_crypto_data()
        if df is None:
            print("❌ API request failed. Retrying in 5 minutes...")
            time.sleep(300)
            continue

        # ✅ Update table (A1:F6)
        sheet.range("A1").value = ["Name", "Symbol", "Price (USD)", "Market Cap", "24h Volume", "24h Change (%)"]
        sheet.range("A2").options(index=False).value = df  # Table update

        # ✅ Add "Live Price" (J3:J8)
        sheet.range("J1").value = "Last Update"
        sheet.range("J2").value = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sheet.range("J3").value = "Live Price (Top 5)"
        sheet.range("J4:J8").value = df[["name", "current_price"]].values  # Top 5 Prices

        wb.app.calculate()  # Force refresh
        print("✅ Excel updated successfully!")

        # ✅ Ensure exactly 5-minute interval
        elapsed_time = time.time() - start_time
        time.sleep(max(0, 300 - elapsed_time))

# Run the Excel update loop
update_excel()
