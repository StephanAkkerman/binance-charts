# Binance Charts
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![MIT License](https://img.shields.io/github/license/StephanAkkerman/Binance_Line_Chart.svg?color=brightgreen)](https://opensource.org/licenses/MIT)

---

> **note**
> I have added this implementation to my more advanced charting repo which you can find [here](https://github.com/StephanAkkerman/live-binance-charts)

## Features
After doing the setup, the code will show your spot holdings in the same style as Tradingview.
9 charts will be created, if you have less than 9 different spot holdings the other charts will be filled up with the most popular coins.
At the moment these coins are "BTCUSDT", "ETHUSDT", "XRPUSDT", "BNBUSDT", "DOGEUSDT", "ADAUSDT", "DOTUSDT", "BCHUSDT", "LTCUSDT". If you like to use other coins as default, then change the default list on line 43.

## Dependencies
The required packages to run this code can be found in the `requirements.txt` file. To run this file, execute the following code block:
```
$ pip install -r requirements.txt 
```
Alternatively, you can install the required packages manually like this:
```
$ pip install <package>
```

## How to run
This code works like most of my other Binance related codes:
- Clone the repository
- Find your Binance API keys and put them in the `src/keys.py` file
- Run `$ python src/main.py`
- See result

## Note
As stated in the description, this project uses mplfinance. Unfortunately, this is not the most efficient library for updating charts. The current refresh rate is set at 5 seconds, so all the charts are updated every 5 seconds. This can be set to a lower value, but that could lead to performance issues, for instance where the charting program freezes. If you would like a more detailed version of this project, check out https://github.com/StephanAkkerman/Live_Binance_Charts it has the same idea, but with more functions and is quicker.

### Base pair
The code uses USDT as base pair. If you would like to use something else, for instance BTC, change the default list and the workings of how the holdings are gotten.

### Futures and margin
At the moment future and margin holdings are not supported, this might be implemented in the future.\

## Screenshot
![Image of screenshot](https://github.com/StephanAkkerman/Binance_Charts/blob/main/img/Screenshot.png)
