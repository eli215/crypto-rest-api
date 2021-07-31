# Crypto RESTful API
A simple demo RESTful API for cryptocurrency trading data.   
  
This project was meant as an introduction to REST APIs. My goal was to get experience building out REST functionality for an existing dataset. The static dataset used for this demo was cryptocurrency trading data obtained from https://www.cryptodatadownload.com/data/ and stored in a local MongoDB instance upon which the API is built.  
Note: I chose the cryptocurrency dataset because it is an area of interest to me, but the demo could've involved any arbitrary dataset.  
  
Status: in progress (as of 3/2021)  
  
## Endpoints

### `/api/exchanges` (not yet implemented)
Returns info about all available crypto exchanges for which data is available.  
Example:  
`GET http://localhost:5001/api/exchanges`  
Response:  
```
{
    "data": [
        {
            "id": "Binance"
        },
        {
            "id": "Kucoin"
        },
        {
            "id": "OKEX"
        },
        ...
    ]
}
```
  
### `/api/exchanges/<exchange>` (not yet implemented)
Returns info about a specific exchange.  
Example:  
`GET http://localhost:5001/api/exchanges/Binance`  
Response:  
```
{
    "data": [
        {
            "id": "Binance"
        }
    ]
}
```
  
### `/api/exchanges/<exchange>/pairs` (in progress)
Returns info about all available trading pairs on a given exchange. For this barebones example, currenly only the `id` and `symbol` is displayed, but additional attributes such as current trading price could be added.  
Example:  
`GET http://localhost:5001/api/exchanges/Binance/pairs`  
Response:  
```
{
    "data": [
        {
            "id": "ADABTC",
            "symbol": "ADA/BTC",
            "last_price": "2.12E-05"
        },
        {
            "id": "BNBUSDT",
            "symbol": "BNB/USDT"
            "last_price": "313.90"
        },
        {
            "id": "BTCUSDT",
            "symbol": "BTC/USDT",
            "last_price": "59109.89"
        },
        ...
    ]
}
```
  
### `/api/exchanges/<exchange>/pairs/<id>` (not yet implemented)
Returns current info about a specific trading pair on a given exchange.  
Example:  
`GET http://localhost:5001/api/exchanges/Binance/pairs/BTCUSDT`  
Response:  
```
{
    "data": [
        {
            "id": "BTCUSDT",
            "symbol": "BTC/USDT",
            "last_price": "59109.89"
        }
    ]
}
```
  
### `/api/exchanges/<exchange>/pairs/<id>/YYYY/MM/DD/HH:mm?interval=<day/hour/minute>` (not yet implemented)
Returns trading pair price info for a specified time interval (`day`, `hour`, or `minute`) ending at a certain time (if available).  
  
Note: the data comes in a form such that additional calculations would be required to get a daily interval with hour-precision, or an hourly interval with minute-precision. To keep it simple, the provided datetime will be truncated to the precision of the specified interval. For example,  
`...2021/12/25/8:25?interval=day` would ignore the time `8:25` and return data for daily interval ending at `2021/12/25/0:00`.  
  
Example:  
`GET http://localhost:5001/api/exchanges/Binance/pairs/ETHBTC/2021/3/3?interval=day`  
Response:  
```
{
    "data": [
        {
            "date": "3/4/2021 0:00"
            "symbol": "ETH/BTC",
            "open": "0.030699",
            "high": "0.031891",
            "low": "0.030663",
            "close": "0.031194",
            "Volume ETH": "314426.426",
            "Volume BTC": "9858.13758",
            "tradecount": "329754"
        }
    ]
}
``` 
