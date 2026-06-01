import yfinance as yf
import matplotlib.pyplot as plt

period_options = [
    "1d",
    "5d",   
    "1mo",  
    "3mo",  
    "6mo",  
    "1y",   
    "2y",   
    "5y"
]

def get_stock_data(ticker="AAPL", period="1y"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)
    return df

def add_sma(df):
    df["SMA20"] = df["Close"].rolling(window=20).mean()
    df["SMA50"] = df["Close"].rolling(window=50).mean()
    return df

def plot_stock(df, ticker="AAPL"):
    plt.figure(figsize=(12,6))

    plt.plot(df.index, df["Close"], label="Close Price")
    plt.plot(df.index, df["SMA20"], label="SMA 20", linewidth=2)
    plt.plot(df.index, df["SMA50"], label="SMA 50", linewidth=2)

    plt.title(f"{ticker} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    # ticker = "AAPL"

    ticker = input("Enter ticker (e.g. AAPL): ").upper()
    period = input("Enter period (1d, 5d, 1mo, 6mo, 1y, 5y): ")


    df = get_stock_data(ticker, "1y")
    df = add_sma(df)
    plot_stock(df, ticker)