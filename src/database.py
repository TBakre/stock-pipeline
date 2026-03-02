import psycopg2 
from src.config import DB_CONFIG 

# Connecting to database
def get_connection(): 
    """  
    Creates and returns a connection to the database 

    """ 
    # ** <- dictionairy unpacking 
    return psycopg2.connect(**DB_CONFIG) 

def save_stock_quotes(df): 
    """ 
    Takes a dataframe  of stock quotes and saves each row to the datbase 

    """ 
# Connect -> cursor -> execute -> commit -> close
    conn = get_connection() 
    cursor = conn.cursor()  

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO stock_quotes 
                (symbol, price, volume, change_percent, timestamp)
            VALUES 
                (%s, %s, %s, %s, %s)
        """, (
            row["symbol"],
            row["price"],
            row["volume"],
            row["change_percent"],
            row["timestamp"]
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Saved {len(df)} records to database!")
  
