import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fix_yahoo_finance as yf
from selenium.webdriver.common.keys import Keys
data = yf.download(
        tickers="HSBC",
        period="1y",
        interval="1wk",
        group_by="ticker")
data['Adj Close'].plot(label='Price')
plt.show()
data['Volume'].plot(label='Vol')
plt.show()

#Could not find the symbols of the stocks, hence could not test for multiple stocks.
# But logic will be same as i get the symbols then i can pass multiple values in tickers and plot the graph for
#each stock and evaluate based on pricing and volume
