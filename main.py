# Python Code for Paper Trader
# CJG Projects
# Python 3.8
# Paper Trader Version 2.0

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
# print("Trading Bot Not Currently Active - Check Other Branch \n")



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


# ------------------------------------- Commands to Sell/Buy Same Stocks to Portfolio --------------------------------

active = ""
found_stock = False
while active.lower() != "yes" or while active.lower() != "no":
    active = input("Do you want to sell or buy any of your currently held stocks? \n yes or no: ")
    print("\n")
if active.lower() == "no":
    print("Okay, you have chosen to not change your portfolio \n")
while active.lower() == "yes":
    whichstock = input("\n Type the abbreviation of the stock you would like to buy or sell. \n Stock Abbreviation: ")

    for each in port['stock']:  # Checking for if the stock has been added in the past
        if each == whichstock:
            found_stock = True

    if found_stock == True:   # This is the code to add the stock if it has already been added before
        buy_or_sell = input("Do you wish to buy or sell the stock? ")
        quantity = input("Quantity: ")
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

    else:  # This is the section for if the stock isn't in the portfolio.  This code adds it.
        to_add = pd.DataFrame(
        {'stock': [whichstock], 'live_price': [si.get_live_price(whichstock)], 'quantity': [0], 'value_now': [0], 'current_invest': [0],
         'loss/gain': [0]})
    port = port.append(to_add, ignore_index=True)

    active = input("\n Do you want to sell or buy any additional of your current stocks? (yes or no) ")


port = port.round(0)
print("Updated Portfolio: \n \n")
print(port)

print("\n \n")
print("Saving Current (Updated) Portfolio....")
port.to_csv('my_stock.csv', index=False)