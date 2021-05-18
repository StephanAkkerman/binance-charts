# Setup
This code works like most of my other Binance related codes.

1. Find your Binance API keys and put them in the keys.py file
2. Make sure BinanceData.py and keys.py are in the same directory

# Use case
After doing the setup, the code will show your spot holdings in the same style as Tradingview.
9 charts will be created, if you have less than 9 different spot holdings the other charts will be filled up with the most popular coins.
At the moment these coins are "BTCUSDT", "ETHUSDT", "XRPUSDT", "BNBUSDT", "DOGEUSDT", "ADAUSDT", "DOTUSDT". If you like to use other coins as default, then change the default list on line 37.

# Updating the charts
As stated in the description, this project uses mplfinance. Unfortunately, this is not the most efficient library for updating charts. The current refresh rate is set at 5 seconds, so all the charts are updated every 5 seconds. This can be set to a lower value, but that could lead to performance issues, for instance where the charting program freezes.

# Screenshot
![Image of screenshot](https://github.com/StephanAkkerman/Binance_Charts/blob/main/Pics/Screenshot.png)
