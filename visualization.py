import pandas as pd
import matplotlib.pyplot as plt

def file_print(data:dict):
    #Prints the data to 
    # -each stock into an excel and a csv file
    # -all stocks into a txt file
    for stock in data:
        data[stock].to_excel(f'{stock}.csv')
        data[stock].to_csv(f'{stock}.csv')
    
    with open(f'{stock}.txt', 'w') as f:
        for stock in data:
            f.write(f'{stock}\n')
            f.write(f'{data[stock]}\n\n')
    

def plot_stock(stock:pd.DataFrame, stock_name:str, SMA1:int , SMA2:int, EMA1:int, EMA2:int): 
    #Plotting the stock data
    plt.figure(figsize=(12,6))
    plt.plot(stock['Close'], label=stock_name)
    plt.plot(stock[f'SMA{SMA1}'], label=f'SMA{SMA1}')
    plt.plot(stock[f'SMA{SMA2}'], label=f'SMA{SMA2}')
    plt.plot(stock[f'EMA{EMA1}'], label=f'EMA{EMA1}')
    plt.plot(stock[f'EMA{EMA2}'], label=f'EMA{EMA2}')
    plt.title(f'{stock_name} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')
    plt.show()