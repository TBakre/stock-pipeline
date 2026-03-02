from src.fetcher import fetch_all_stocks 
from src.database import save_stock_quotes 

def main():  
    print("Starting stock pipline...")
    
    df = fetch_all_stocks()  
    print(df)

    save_stock_quotes(df) 
    print("Pipeline Complete")

if __name__ == "__main__": 
    main()
