# Python Code for Paper Trader
# CJG Projects
# Python 3.8

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
print("Trading Bot Not Currently Active - Check Other Branch \n")



for each in port['stock']:
    port['live_price'][i] = si.get_live_price(each)
    i += 1


# print(port)

port['value_now'] = port['live_price'] * port['quantity']
port['loss/gain'] = port['current_invest'] + port['value_now']

port = port.round(0)
print(port)

total_profit = port['loss/gain'].sum()
print("\n")
print("Total Profit: ")
print(total_profit)

while xyz.lower() != "yes":
    xyz = input("Continue? ")
    print("\n")


# ------------------------------------- Commands to Add new Stocks to Portfolio -------------------------------------

time.sleep(1)   #  This Section is In Progress  --  It can currently be done by adding the stock manually to the csv file.
print("The next section allows you to add new stocks to the portfolio.  This can be done manually by addind information to the csv. \n")
print("This section is currently being worked on to automate the process.")

print("This next section is for adding new stocks to the csv that have never been in the portfolio")
print("If a stock have ever been part of the CSV, the stock name is saved and you can buy or sell using the previous section. \n"
      "Even if the quanity is 0.")
print("\n \n")

addingstock_answer = input("Would you like to add any stocks to the portfolio that are not currently in it? \n (yes or no) \n ")

while addingstock_answer.lower() == "yes":
    time.sleep(1)
    stockabbrev = input("\nWhat is the abbreviation of the stock? \n")
    to_add = pd.DataFrame(
        {'stock': [stockabbrev], 'live_price': [si.get_live_price(stockabbrev)], 'quantity': [0], 'value_now': [0], 'current_invest': [0],
         'loss/gain': [0]})
    port = port.append(to_add, ignore_index=True)
    addingstock_answer = input("Would you like to add any other new stocks? \n")


port = port.round(0)
print("Saving Portfolio.....")
port.to_csv('my_stock.csv', index=False)
print("\nUpdated Portfolio: \n \n")
print(port)
print("\n \n")

# ------------------------------------- Commands to Sell/Buy Same Stocks to Portfolio --------------------------------

active = input("Do you want to sell or buy any of your currently held stocks? (yes or no) \n")
if active.lower() != "yes":
    print("\n")
    print("Okay you have chosen not to add any stocks....")
    time.sleep(1)
while active.lower() == "yes":
    whichstock = input("\n Which Stock would you like to buy/sell? (must be in your current portfolio.) \n ")
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
    active = input("\n Do you want to sell or buy any additional of your current stocks? (yes or no) ")


port = port.round(0)
print("Updated Portfolio: \n \n")
print(port)

print("\n \n")
print("Saving Current (Updated) Portfolio....")
port.to_csv('my_stock.csv', index=False)
