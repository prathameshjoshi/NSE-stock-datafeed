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

    print(symbol)
    data_30_minute = tv.get_hist(symbol,'NSE',interval=Interval.in_30_minute,n_bars=10000) # Download Data
    data_30_minute.drop(['symbol'], axis = 1) # drop symbol column
    data_30_minute.to_csv('Datafeed/' + symbol + '_30_minute.csv') # Store into csv file

githubcommit.git_commit()
