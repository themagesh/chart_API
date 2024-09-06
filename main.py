from fastapi import FastAPI, HTTPException
import requests
import os

API_KEY='d21b71d1-0cf3-4eb5-a126-836422cdbb50'



app = FastAPI()

# CoinMarketCap API URL and parameters
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {'symbol': 'BTC', 'convert': 'USD'}
headers = {'X-CMC_PRO_API_KEY': API_KEY}

@app.get("/bitcoin-price")
async def get_bitcoin_price():
    try:
        # Make API call to CoinMarketCap
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()
        print(data)
        if response.status_code == 200:
            # Extract Bitcoin price in USD
            btc_price = data['data']['BTC']['quote']['USD']['price']
            return {"Bitcoin Price (USD)": btc_price}
        else:
            # Handle error if request failed
            raise HTTPException(status_code=response.status_code, detail=data.get("status", {}).get("error_message", "Unknown Error"))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run the app using Uvicorn
# uvicorn main:app --reload
