# This file holds the basic function to update the portfolio for the initial part of the paper trader
import pandas as pd
from yahoo_fin import stock_info as si

def update_port():
    pd.options.mode.chained_assignment = None
    # The following two lines are for setting up the moving averages for the trading bot in the future
    # currentDT = dt.datetime.now()
    # today = date.today()

    # This actually updates the Portfolio.
    port = pd.read_csv('my_stock.csv')
    i = 0
    for each in port['stock']:
        port['live_price'][i] = si.get_live_price(each)
        i += 1

    port['value_now'] = port['live_price'] * port['quantity']
    port['loss/gain'] = port['current_invest'] + port['value_now']

    port = port.round(0)
    print(port)

    total_profit = port['loss/gain'].sum()
    print("\n")
    print("Total Profit: ")
    print(total_profit)
    return port


