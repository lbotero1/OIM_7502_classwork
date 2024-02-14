import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import seaborn as sb
sb.set_theme()

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()


    def get_data(self):
        import yfinance as yf
        data = yf.download(self.symbol, start=self.start, end=self.end)
        data.index = pd.to_datetime(data.index)
        data.index.name = 'date'
        self.calc_returns(data)
        return data
        pass
        # method that downloads data and stores in a DataFrame
           # uncomment the code below wich should be the final two lines
           # of your method"""

    
    def calc_returns(self, df):
        df['Change'] = df['Close'].diff()
        df['Return'] = np.log(df['Close']).diff().round(4)
        # """method that adds change and return columns to data"""
        pass

    
    def plot_return_dist(self):
        self.data['Return'].hist(bins=50, alpha=0.6)
        plt.show()
        # """method that plots instantaneous returns as histogram"""
        pass


    def plot_performance(self):
        self.data['Cumulative Return'] = (1 + self.data['Return']).cumprod() - 1
        self.data['Cumulative Return'].plot()
        plt.show()
        # """method that plots stock object performance as percent """
        pass
                

def main():
    symbol = "META"
    # uncomment (remove pass) code below to test
    test = Stock(symbol=['AAPL']) # optionally test custom data range
    print(test.data)
    test.plot_performance()
    test.plot_return_dist()
    pass

if __name__ == '__main__':
    main()