"""
Name:  Tomas Castro
Email: [Your Email]
Stock Market Analyzer - Work in Progress
Currently supports: single stock price visualization
Coming soon: correlation analysis, moving averages, portfolio tracker
"""

import pandas as pd
import plotly.express as px

# NOTE: requires yfinance — install with: pip install yfinance
import yfinance as yf

# ── SECTION 1: LOAD STOCK DATA (WORKING) ─────────────────────────────────────

def get_stock_data(ticker, period="1y"):
    """Download stock price history for a given ticker symbol."""
    print(f"Fetching data for {ticker}...")
    stock = yf.download(ticker, period=period)
    return stock

# ── SECTION 2: BASIC PRICE CHART (WORKING) ───────────────────────────────────

def plot_price(ticker):
    """Plot closing price over time for a stock."""
    df = get_stock_data(ticker)
    df = df.reset_index()

    fig = px.line(df,
                  x="Date",
                  y="Close",
                  title=f"{ticker} Stock Price — Last 12 Months",
                  labels={"Close": "Closing Price (USD)", "Date": "Date"})
    fig.show()
    fig.write_html(f"{ticker}_price_chart.html")
    print(f"Chart saved as {ticker}_price_chart.html")

# ── SECTION 3: BASIC STATS (WORKING) ─────────────────────────────────────────

def print_stats(ticker):
    """Print basic stats for a stock."""
    df = get_stock_data(ticker)
    print(f"\n--- {ticker} Stats (Last 12 Months) ---")
    print(f"Highest price : ${df['Close'].max():.2f}")
    print(f"Lowest price  : ${df['Close'].min():.2f}")
    print(f"Average price : ${df['Close'].mean():.2f}")
    print(f"Total trading days: {len(df)}")

# ── SECTION 4: MOVING AVERAGES (IN PROGRESS) ─────────────────────────────────

# TODO: Add 50-day and 200-day moving averages to the price chart
# This will help identify bullish/bearish trends
#
# def plot_moving_averages(ticker):
#     df = get_stock_data(ticker)
#     df['MA50']  = df['Close'].rolling(window=50).mean()
#     df['MA200'] = df['Close'].rolling(window=200).mean()
#     # plotting code coming soon...

# ── SECTION 5: STOCK CORRELATION (IN PROGRESS) ───────────────────────────────

# TODO: Compare multiple stocks and show how correlated they are
# For example: does Apple move with Microsoft? Does the market move together?
#
# def plot_correlation(tickers):
#     all_data = {}
#     for ticker in tickers:
#         df = get_stock_data(ticker)
#         all_data[ticker] = df['Close']
#     combined = pd.DataFrame(all_data)
#     correlation = combined.corr()
#     # heatmap code coming soon...

# ── SECTION 6: PORTFOLIO TRACKER (NOT STARTED YET) ───────────────────────────

# TODO: Let user input a list of stocks and quantities they own
# Then calculate total portfolio value over time
# and show gains/losses as a chart
#
# def portfolio_tracker(holdings):
#     # holdings = {'AAPL': 10, 'MSFT': 5, 'NVDA': 3}
#     # code coming soon...
#     pass

# ── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Currently working — run this to see the price chart
    ticker = input("Enter a stock ticker (e.g. AAPL, MSFT, NVDA): ").upper()
    print_stats(ticker)
    plot_price(ticker)
