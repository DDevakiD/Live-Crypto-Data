# Live-Crypto-Data

A Python project that fetches live cryptocurrency market data from the CoinGecko API and provides two main functionalities:

- **Excel Update:** Continuously updates a local Excel file (`CoinGecko111.xlsx`) with live data of the top 5 cryptocurrencies by market cap every 5 minutes using `xlwings`.
- **Live Plot:** Displays a live-updating bar chart of the top 5 cryptocurrencies by market cap, refreshing every 5 minutes using `matplotlib`.

---

## Features

- Fetches real-time crypto data (name, symbol, price, market cap, volume, and 24h price change).
- Updates Excel sheet dynamically without freezing.
- Visualizes live crypto prices in a bar chart.
- Handles API errors with retries.
- Automatic 5-minute interval updates.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Live-Crypto-Data.git
   cd Live-Crypto-Data


Install required Python packages:

bash
Copy
Edit
pip install requests pandas xlwings matplotlib
Make sure you have Excel installed (required for xlwings).

Usage
Excel Update Script
Run the Python script that updates the Excel file with live data every 5 minutes:

bash
Copy
Edit
python excel_update.py
Opens or creates CoinGecko111.xlsx.

Updates the "Sheet1" with live crypto data every 5 minutes.

Shows the last update timestamp and live prices in specified cells.

Live Plot Script
Run the Python script that shows a live-updating bar chart of top 5 cryptocurrencies by market cap:

bash
Copy
Edit
python live_plot.py
Opens a matplotlib window showing top 5 cryptocurrencies by market cap.

Automatically refreshes the plot every 5 minutes with live data.

API Used
CoinGecko API - Markets Endpoint

