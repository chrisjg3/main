# CJG Projects ~ Trading Bot
# Python 3

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from datetime import date
import time
from yahoo_fin import stock_info as si

# ------------------------------------- Commands to Read Portfolio ---------------------------------

print("Algorithmic Trading Bot - CJG")

port = pd.read_csv('tradingBot/bot_stock.csv')
wait_to_continue = ""
pd.options.mode.chained_assignment = None

# Setting 50ma and 100ma to 0 so the the 1st printed portfolio doesn't have misinformation.
port['50ma'] = 0
port['100ma'] = 0

# Preparing for creating updated 50ma and 100ma variables
hundred_days = dt.timedelta(100)
fifty_days = dt.timedelta(50)
end = dt.datetime.now()
start = end - hundred_days

# This "money_sunk" essentially is the max the bot will be allowed to invest per stock.
# It is essentially the lower limit on the 'current_invest' column. 
money_sunk = -10000.0  

i = 0
for each in port['stock']:
    port['live_price'][i] = si.get_live_price(each)
    i += 1


print("Current Portfolio with live_prices")
print(port)      

# Updating 50ma and 100ma while user looks at portfolio with live prices from previous print(port)
i = 0
for each in port['stock']:
    df = web.DataReader(each, 'yahoo', start, end)['Adj Close']
    df = df.drop(columns=['Date'])
    port['100ma'][i] = df.mean()
    df = df.tail(50)
    port['50ma'][i] = df.mean()
    i += 1


print("\n\n")
print("Portfolio with 50ma and 100ma:")
print(port)
print("\n\n")

while wait_to_continue != "yes":
    print("\n \n")
    wait_to_continue = input("Continue? \n")

# ------------------------------------- Customizing Bot and Portfolio -------------------------------------

print("\n \nBot Customization\n \n")

addingstock_answer = input("Would you like the trading bot to look into any additional stocks? \n (yes or no) \n ")
while addingstock_answer.lower() == "yes":
    stockabbrev = input("\nWhat is the abbreviation of the stock? \n")
    to_add = pd.DataFrame(
        {'stock': [stockabbrev], 'live_price': [si.get_live_price(stockabbrev)], 'quantity': [0], 'value_now': [0], 'current_invest': [0],
         'loss/gain': [0]})
    port = port.append(to_add, ignore_index=True)
    addingstock_answer = input("Would you like to add any other new stocks? \n")


customize_option = input("Would you like to edit the bot's settings? (yes or no) \n")
while customize_option.lower() != "no":
    max_amount = input("What is the max amount you want the bot to be able to invest PER STOCK? (Default is set to 10000) \n")
    try:
        if float(max_amount) > 0:
            money_sunk = -1 * (float(max_amount))
        money_sunk = (float(max_amount))
        print("Max Amount set to: " + str(max_amount))
        print("This means the bot will not drop below -" + str(max_amount) +" in the \"Current Invest\" column.")
    except:
        print('Error, not a valid amount')
        print("Max remains 10000")
    print("\n \n")
    allow_shorts = input("Would you like the bot to be able to short stock? \n"
                         "(this feature currently not incorporated yet, type anything answer to continue) \n")
    if allow_shorts.lower() == "yes":
        shorts_on = True
    elif allow_shorts.lower() == "no":
        shorts_on = False
    else:
        print("Invalid answer: Bot will not be allowed to short.")
        shorts_on = False
    customize_option = input("Would you like to change any of the customization again? ")

print("\n \n \n")

# ------------------------------------- Functions Behind Bot Code -------------------------------------

import bot_sell_buy as bsb

port = bsb.buy_stock(port, money_sunk)

port = bsb.sell_stock(port)

port = port.round(2)
print('After bot editted Portfolio: ')
print(port)

port.to_csv('tradingBot/bot_stock.csv', index=False)
