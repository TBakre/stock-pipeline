import os 
from dotenv import load_dotenv 

#loading variables from my .env file into the program  
load_dotenv() 

#API Configuration 
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY") 
BASE_URL = "https://www.alphavantage.co/query" 

# Stocks to track 
STOCKS = ["AAPL", "GOOGL", "MSFT", "AMZN"]

# Database configuration  
DB_CONFIG = { 
    "host" : "localhost", 
    "database": "stock_pipeline" , 
    "user" : "postgres" ,  
    "password": "postgres", 
    "port" : 5433

}