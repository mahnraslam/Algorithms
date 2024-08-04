import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

dict_={'a':[11,21,31],'b':[12,22,32]}
df=pd.DataFrame(dict_)
print(type(df))

cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
print(type(bitcoin_data))

bitcoin_price_data = bitcoin_data['prices']
print(bitcoin_price_data[0:10])

data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms').dt.date

candlestick_data = data.groupby('Date', as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})

fig = go.Figure(data=[go.Candlestick(x=candlestick_data['Date'],
                                     open=candlestick_data['Price']['first'], 
                                     high=candlestick_data['Price']['max'],
                                     low=candlestick_data['Price']['min'], 
                                     close=candlestick_data['Price']['last'])
                     ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()

# # Save the plot as an HTML file
# plot(fig, filename='candlestick_chart.html', auto_open=False)

# Save the plot as a static image
fig.write_image("candlestick_chart.png")
