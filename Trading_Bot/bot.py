# CJG Projects ~ Trading Bot
# Python 3
# Still a work in progress, but the basic skeleton is there.

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from datetime import date
import time
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
from matplotlib import style

# ------------------------------------- Commands to Read Portfolio ---------------------------------

print("Algorithmic Trading Bot - CJG")
currentDT = dt.datetime.now()
today = date.today()
port = pd.read_csv('my_stock.csv')
i = 0
xyz = ""
pd.options.mode.chained_assignment = None

style.use('ggplot')

hundred_days = dt.timedelta(100)
fifty_days = dt.timedelta(50)
end = dt.datetime.now()
start = end - hundred_days
max_amount = 1000.0

port['100ma'] = 0
port['50ma'] = 0

for each in port['stock']:
    port['live_price'][i] = si.get_live_price(each)
    i += 1

print(port)        #I seperated caluclating the 'live price' out so that the portfolio can be viewed while the 100ma and 50ma are calculated.

for each in port['stock']:
    df = web.DataReader(each, 'yahoo', start, end)['Adj Close']
    df = df.drop(columns=['Date'])
    port['100ma'][i] = df.mean()
    df = df.tail(50)
    port['50ma'][i] = df.mean()
    i += 1

print(port)

while xyz != "yes":
    print("\n \n")
    xyz = input("Continue? \n")

# ------------------------------------- Customizing Bot and Portfolio -------------------------------------
print("\n \nBot Customization\n \n")

addingstock_answer = input("Would you like to add any stocks to the portfolio that are not currently in it? \n (yes or no) \n ")
while addingstock_answer.lower() == "yes":
    stockabbrev = input("\nWhat is the abbreviation of the stock? \n")
    to_add = pd.DataFrame(
        {'stock': [stockabbrev], 'live_price': [si.get_live_price(stockabbrev)], 'quantity': [0], 'value_now': [0], 'current_invest': [0],
         'loss/gain': [0]})
    port = port.append(to_add, ignore_index=True)
    addingstock_answer = input("Would you like to add any other new stocks? \n")


customize_option = input("Would you like to edit the bot's settings? \n")
while customize_option != "no":
    max_amount = input("What is the max amount you want the bot to be able to spend PER STOCK? (Default is set to 1000) \n")
    try:
        max_amount = float(max_amount)
        print("Max Amount set to: " + str(max_amount))
    except:
        print('Error, not a valid amount')
        print("Max remains 1000")
    print("\n \n")
    allow_shorts = input("Would you like the bot to be able to short stock? \n"
                         "Keep in mind, puts in this paper trader don't work exactly like puts in the real world. \n")
    if allow_shorts.lower() == "yes":
        shorts_on = True
    elif allow_shorts.lower() == "no":
        shorts_on = False
    else:
        print("Invalid answer: set to false")
        shorts_on = False
    customize_option = input("Continue to customize?")

print("\n \n \n")

# ------------------------------------- Functions Behind Bot Code -------------------------------------

def buy_stock(row):
    print("\n" + str(row))
    if row == 0:
        row = (max_amount * 2) + 1
    order_amount = max_amount / row
    order_amount = round(order_amount, 0)
    return int(order_amount)


# ------------------------------------- Trading Bot Code -------------------------------------
print('\n')
print('Before Bot')
print(port)
print('\n \n \n')
for row in pd.read_csv('my_stock.csv', chunksize=1):
    if row['50ma'] > row['100ma']:
        for price in row['live_price']:
            quantity = quantity + buy_stock(price)

print('after bot')
print(port)
