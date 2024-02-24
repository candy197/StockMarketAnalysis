from datetime import date
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
from jugaad_data.nse import NSELive
import yfinance as yf
import pandas as pd 

# Download bhavcopy
#bhavcopy_save(date(2024,1,25), "./")

# Download bhavcopy for futures and options
#bhavcopy_fo_save(date(2024,1,25), "./")

# Get live Nifty 50 data
nifty_50 = yf.Ticker("^NSEI")

# Extract low and high prices
nifty_low = nifty_50.info["regularMarketDayLow"]
nifty_high = nifty_50.info["regularMarketDayHigh"]

# Get a list of Nifty 50 companies from Wikipedia
nifty_companies = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS",  # Add more companies here
                   "HINDUNILVR.NS", "SBIN.NS", "KOTAKBANK.NS", "BHARTIARTL.NS", "LT.NS"
                   ]

# Get prices of all companies in Nifty 50
nifty_company_prices = yf.download(nifty_companies, period="1d", group_by="ticker")

# Print the results
print("Nifty 50 Low:", nifty_low)
print("Nifty 50 High:", nifty_high)
print("Nifty 50 Company Prices:")

df = pd.DataFrame(nifty_company_prices)



for company, price in nifty_company_prices.items():
    print(f"- {company}: {price}")



df.to_csv("stock.csv")

print(df)