import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import numpy as np
import time
from matplotlib.animation import FuncAnimation
from binance.client import Client

# Dont forget to place these in the same directory
from BinanceData import fetchData
import keys

# IDEAS:
# Trend lines (https://github.com/matplotlib/mplfinance/blob/master/examples/using_lines.ipynb)
# Plot stop loss hlines
# Use futures account positions

# Save your API keys in keys.py
client = Client(keys.public_key, keys.private_key)

# Get current holdings and save in owned
# Returns list of dictionary of all the orders that are open
open_order = client.get_open_orders()
   
# Convert it to a pandas dataframe
orders_df = pd.DataFrame(open_order)

# Filter on 'type': 'STOP_LOSS_LIMIT', take only the symbols, convert it to list
try:
    owned = orders_df[orders_df['type']=='STOP_LOSS_LIMIT']['symbol'].tolist()
# In case there are no active stop_loss_limit orders
except Exception as e: 
    pass

# === Default list ===
# List to use when owned consists of less than 9 items
default = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "BNBUSDT", "DOGEUSDT", "ADAUSDT", "DOTUSDT"]

# =========================
# =====   PLOTTING    =====
# =========================

# === TRADINGVIEW STYLE ===
# https://github.com/matplotlib/mplfinance/blob/master/examples/styles.ipynb
mc = mpf.make_marketcolors(up='#2e7871',down='#e84752',inherit=True)

s  = mpf.make_mpf_style(
                        base_mpf_style='nightclouds',
                        y_on_right=True,
                        marketcolors=mc,facecolor='#131722',
                        edgecolor='#4a4e59',
                        figcolor='#131722',
                        gridstyle='solid',
                        gridcolor='#1d202b')

fig = mpf.figure(style=s,figsize=(20,8))

# === CREATE PLOTS ===
#https://github.com/matplotlib/mplfinance/blob/master/examples/external_axes.ipynb

axs = []

# 9 plots
for x in range(1,10):
    axs.append(fig.add_subplot(3,3,x))

#https://github.com/matplotlib/mplfinance/blob/master/examples/plot_customizations.ipynb
#https://stackoverflow.com/questions/60599812/how-can-i-customize-mplfinance-plot

# This function gets called every x ms
def animate(counter):

    # Latest 100 candles
    i = 0
    default_counter = 0

    for ax in axs:

        try:
            symbol = owned[i]

        # List index out of range
        # Use default list
        except Exception as e: 
            if default[default_counter] not in owned:
                symbol = default[default_counter]
            default_counter += 1

        data = fetchData(symbol, 1, '15m')[-100:]

        # Clear old plot
        ax.clear()

        # Set title of every plot
        ax.set_title(symbol)
        ax.yaxis.get_major_formatter().set_scientific(False)

        current_price = data['close'].iloc[-1]
        old_price = data['close'].iloc[-2]

        if current_price > old_price:
            color = 'green'
        if current_price == old_price:
            color = 'gray'
        if current_price < old_price:
            color = 'red'

        # Draw current price
        ax.text(101,
                current_price, 
                f"{np.format_float_positional(current_price)}", 
                color="white", 
                ha="left", 
                va="center", 
                bbox=dict(facecolor=color, alpha=0.5))

        if i > 5:
            mpf.plot(
                    data,
                    ax=ax,
                    volume=False, 
                    type='hollow_and_filled',
                    #Plot time on x-axis
                    datetime_format='%H:%M', 
                    ylabel='', 
                    tight_layout=True, 
                    # Price Line
                    hlines=dict(hlines=current_price,linestyle='dashed',linewidths=(1)),
                    )
        else:
            mpf.plot(
                    data,
                    ax=ax,
                    volume=False,
                    type='hollow_and_filled',
                    datetime_format='',
                    ylabel='', 
                    tight_layout=True, 
                    hlines=dict(hlines=current_price,linestyle='dashed',linewidths=(1)),
                    )

        i = i+1

# Update every 5 seconds (1 sec = 1000ms)
ani = FuncAnimation(fig, animate, interval=5000)

plt.show()