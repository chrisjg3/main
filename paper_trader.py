
# This is the file for the actual
# portfolio
# CJG Projects

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from datetime import date
import time
from yahoo_fin import stock_info as si


# ------------------------------------- Commands to Read Portfolio ---------------------------------

print("Stock Software - CJG")
time.sleep(1)
print("Current Portfolio: ")
currentDT = dt.datetime.now()
today = date.today()
port = pd.read_csv('my_stock.csv')
i = 0
xyz = ""
pd.options.mode.chained_assignment = None



for each in port['stock']:
    port['live_price'][i] = si.get_live_price(each)
    i += 1


# print(port)

port['value_now'] = port['live_price'] * port['quantity']
port['loss/gain'] = port['current_invest'] + port['value_now']

print(port)

total_profit = port['loss/gain'].sum()
print("\n")
print("Total Profit: ")
print(total_profit)

while xyz.lower() != "yes":
    xyz = input("Continue? ")

# ------------------------------------- Commands to Sell/Buy Same Stocks to Portfolio --------------------------------

time.sleep(1)
active = input("Do you want to sell or buy any of your currently held stocks? (yes or no) \n")
while active.lower() == "yes":
    whichstock = input("\n Which Stock would you like to buy/sell? (must be in your current portfolio.) \n "
                       "Additional stocks can be added later. \n")
    # if port['stocks'].str.contains(str(whichstock).lower()):
    try:
        buy_or_sell = input("Do you wish to buy or sell the stock? \n")
        quantity = input("Please put in the quantity you wish to purchase/sell: \n")
        buyprice = si.get_live_price(whichstock.lower())
        try:
            quantity = int(quantity)
        except:
            print("Must enter an integer.  It has been set to 1.")
            quantity = 1
            time.sleep(1)
        if buy_or_sell.lower() == "buy":
            print("...")
            time.sleep(1)
            port['current_invest'][port[port['stock'] == whichstock].index.item()] = port['current_invest'][port[port['stock'] == whichstock].index.item()] - (buyprice * quantity)
            port['quantity'][port[port['stock'] == whichstock].index.item()] = port['quantity'][port[port['stock'] == whichstock].index.item()] + quantity
            print("\nProcess Complete...\n")
        elif buy_or_sell.lower() == "sell":
            print("...")
            time.sleep(1)
            port['current_invest'][port[port['stock'] == whichstock].index.item()] = port['current_invest'][port[port['stock'] == whichstock].index.item()] + (buyprice * quantity)
            port['quantity'][port[port['stock'] == whichstock].index.item()] = port['quantity'][port[port['stock'] == whichstock].index.item()] - quantity
        else:
            print("\nYou must enter buy or sell. Restarting section...")
    except:
        print("\n Not in Portfolio Error.  Try again.....")
    # else:
    active = input("\n Do you want to sell or buy any additional of your current stocks? (yes or no) ")


time.sleep(1)
print("Updated Portfolio: \n \n")
print(port)

while xyz.lower() != "yes":
    xyz = input("Continue? \n")

print("Saving Current (Updated) Portfolio....")
port.to_csv('my_stock.csv', index=False)
print("\n \n \n")

# ------------------------------------- Commands to Add new Stocks to Portfolio -------------------------------------

time.sleep(1)   #  This Section is In Progress  --  It can currently be done by adding the stock manually to the csv file.
print("The next section allows you to add new stocks to the portfolio.  This can be done manually by addind information to the csv. \n")
print("This section is currently being worked on to automate the process.")