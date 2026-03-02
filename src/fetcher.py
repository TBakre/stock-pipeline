import requests 
import pandas as pd 
from datetime import datetime  
import time
from src.config import API_KEY, BASE_URL, STOCKS 

def fetch_stock_quote(symbol): 

    """ 
    Fetches the current price and vlume for a single stock symbol.
    """ 

    # parameters sent to API  
    params = { 
        "function" : "GLOBAL_QUOTE" , 
        "symbol" : symbol, 
        "apikey" : API_KEY
    } 

    # API call
    response = requests.get(BASE_URL, params=params)
    
    # Convert the response to a Python dictionary
    data = response.json()
    
    # just the quote data we need
    quote = data["Global Quote"]
    
    # Return an organized dictionary with just what we need
    return {
        "symbol": symbol,
        "price": float(quote["05. price"]),
        "volume": int(quote["06. volume"]),
        "change_percent": quote["10. change percent"],
        "timestamp": datetime.now()
    }

def fetch_all_stocks():
    """
    Loops through all stocks in our config and fetches each one
    Returns a pandas DataFrame as a table of all stock data
    """
    
    all_quotes = []
    
    for symbol in STOCKS:
        print(f"Fetching data for {symbol}...")
        quote = fetch_stock_quote(symbol)
        all_quotes.append(quote) 
        time.sleep(15)
    
    # Convert our list of dictionaries into a DataFrame (a table)
    df = pd.DataFrame(all_quotes)
    return df