import credentials
import githubcommit

import pandas as pd
from tvDatafeed import TvDatafeed, Interval

username = credentials.username
password = credentials.password

tv=TvDatafeed(username, password, chromedriver_path='/home/prathamesh/Software/chromedriver/chromedriver')

# Read NSE symbol file
stock_symbol = pd.read_csv('nsesymbol.csv')


for symbol in stock_symbol['d__002']:

    data_3_minute = tv.get_hist(symbol,'NSE',interval=Interval.in_3_minute,n_bars=10000) # Download Data
    data_3_minute.drop(['symbol'], axis = 1) # drop symbol column
    data_3_minute.to_csv('Datafeed/' + symbol + '_3_minute.csv') # Store into csv file

githubcommit.git_commit()
