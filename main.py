# Paper Trader
# CJG Projects
# Python 3.8
# Paper Trader Version 2.0.1

import pandas as pd
import datetime as dt
from datetime import date
import time
from yahoo_fin import stock_info as si
# Below this is modules imported from within this package
from paperTrader import update_portfolio as up
from paperTrader import buy_sell_functions as bsf


# This is the introduction to the program and updates the current live prices.

print("Stock Software - CJG")
time.sleep(1)
print("Current Portfolio: ")
pd.options.mode.chained_assignment = None

port = up.update_port()


check_point = ""
while check_point.lower() != "yes":
    check_point = input("Continue? ")
    print("\n")


# This is where stocks are bought and sold to change the portfolio.


port = bsf.change_port(port)


print("\n \n")
print("Saving Current (Updated) Portfolio....")
port.to_csv('my_stock.csv', index=False)