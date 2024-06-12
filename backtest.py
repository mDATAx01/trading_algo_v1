import stocks_mng as sm
import visualization as vs
import pandas as pd

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

# Print the data
vs.file_print(data)

# Plot the data
for stock in data:
    vs.plot_stock(data[stock], stock, SMA1, SMA2, EMA1, EMA2)

# Backtesting function
def backtest_1(stock: pd.DataFrame, initial_capital:int, shares=int):
    newstock = stock.copy()
    newstock['Holdings'] = stock['Close'] * shares * stock['Signals_1']
    newstock['Cash'] = initial_capital - (stock['Close'] * shares * stock['Position_1']).cumsum()
    newstock['Total'] = stock['Holdings'] + stock['Cash']
    newstock['Returns'] = newstock['Total'].pct_change()
    
    return newstock