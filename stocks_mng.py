import yfinance as yf
import pandas as pd
import numpy as np


#STOCK
                

# Get the data for the stocks  
def getStockData(l_stocks:list, date1:str , date2:str): 
    #date format: 'YYYY-MM-DD'
    #returns a dict of Pandas DataFrame
    data = dict()
    for stock in l_stocks:
        data[stock] = yf.download(stock,date1,date2)

    return data
        
def getAdditionalData_1(stock:pd.DataFrame, SMA1:int , SMA2:int, EMA1:int, EMA2:int):
    #Simple & Exponential Moving Averages (SMAs/EMAs)
    stock[f'SMA{SMA1}'] = stock['Close'].rolling(window=SMA1).mean()
    stock[f'SMA{EMA1}'] = stock['Close'].rolling(window=SMA2).mean()
    stock[f'EMA{EMA1}'] = stock['Close'].ewm(span=EMA1, adjust=False).mean()
    stock[f'EMA{EMA2}'] = stock['Close'].ewm(span=EMA2, adjust=False).mean()

    return stock

def genTradingSignals_1(stock:pd.DataFrame, SMA1:int , SMA2:int, EMA1:int, EMA2:int):
    
    #Get SMAs/EMAs
    stock = getAdditionalData_1(stock, SMA1, SMA2, EMA1, EMA2)

    #Column 'Signals_1' to store the trading signals
    #with 1 for buy signal, -1 for sell signal and 0 for hold signal
    stock['Signals_1'] = 0

    # Bullish signals (Golden Cross:Price Crosses Above EMA)
    stock['Signals_1'][20:] = np.where((stock['EMA20'][20:] > stock['EMA50'][20:]) & 
                                            (stock['Close'][20:] > stock['EMA20'][20:]), 1, 0)
    
    # Bearish signals (Death Cross)
    stock['Signals_1'][20:] = np.where((stock['EMA20'][20:] < stock['EMA50'][20:]) & 
                                            (stock['Close'][20:] < stock['EMA20'][20:]), -1, 0)
    
    #Column 'Position' to store the changes in the signals
    stock['Position_1'] = np.where(stock['Signals_1'].diff() == 1, 'b', #'b' for buy 
                     np.where(stock['Signals_1'].diff() == -1, 's',   #'s' for sell
                     np.where(stock['Signals_1'] == 0, 'h', 0)))      #'h' for hold

    
    return stock