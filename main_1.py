import stocks_mng as sm
import visualization as vs
import backtest as bt


# Get the data for the stocks
stocks = ['AAPL','MSFT','GOOGL']
date1 = '2020-03-15'
date2 = '2024-03-15'
data = sm.getStockData(stocks, date1, date2)

# Generate trading signals
SMA1 = 20
SMA2 = 50
EMA1 = 20
EMA2 = 50
for stock in data:
    data[stock] = sm.genTradingSignals_1(data[stock], SMA1, SMA2, EMA1, EMA2)


# Plot the data & Print the data
vs.file_print(data)
for stock in data:
    vs.plot_stock(data[stock], stock, SMA1, SMA2, EMA1, EMA2)


# Backtest results
initial_capital = 100000
shares = 100
newdata = dict()
for stock in data:
    newdata[stock] = bt.backtest_1(data[stock], initial_capital, shares)
    
vs.file_print(newdata)
for stock in newdata:
    vs.plot_stock(data[stock], stock, SMA1, SMA2, EMA1, EMA2)