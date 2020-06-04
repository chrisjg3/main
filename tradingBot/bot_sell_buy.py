import pandas as pd
# import datetime as dt
# from datetime import date
# import pandas_datareader.data as web
# i = 0

# pd.options.mode.chained_assignment = None
# port = pd.read_csv('tradingBot/test_stock.csv')


# port['50ma'] = 0
# port['100ma'] = 0

# print(port)

# hundred_days = dt.timedelta(100)
# fifty_days = dt.timedelta(50)
# end = dt.datetime.now()
# start = end - hundred_days

# "money_sunk" essentially is the max the bot will be allowed to invest per stock.
# This will appear in the 'current_invest' column
# money_sunk = -10000.0  

# for each in port['stock']:
#     df = web.DataReader(each, 'yahoo', start, end)['Adj Close']
#     df = df.drop(columns=['Date'])
#     port['100ma'][i] = df.mean()
#     df = df.tail(50)
#     port['50ma'][i] = df.mean()
#     i += 1

# print("\n\n\n")
# print(port)
# print("\n\n")




def buy_stock(port, money_sunk):
    which_index = 0
    for each in port['100ma']:
        if each * 1.02 <= port['50ma'][which_index]:
            # If a stock has a signficantly higher 50ma then 100ma, we will buy, but only if not at limit.
            if port['current_invest'][which_index] > money_sunk:
                room_to_invest = port['current_invest'][which_index] - money_sunk
                order_quantity = room_to_invest // port['live_price'][which_index]
                if order_quantity != 0:
                    port['quantity'][which_index] = port['quantity'][which_index] + order_quantity
                    port['current_invest'][which_index] = port['current_invest'][which_index] - (order_quantity * port['live_price'][which_index])
        which_index += 1
    port['value_now'] = port['live_price'] * port['quantity']
    return port


def sell_stock(port):
    which_index = 0
    for each in port['50ma']:
        # If stock is slightly below, it auto sells.
        if each * 1.01 <= port['100ma'][which_index]:
            if port['quantity'][which_index] >= 1:
                port['current_invest'][which_index] = port['current_invest'][which_index] + (port['quantity'][which_index] * port['live_price'][which_index])
                port['quantity'][which_index] = 0
        which_index += 1
    return port


# port.to_csv('tradingBot/test_stock.csv', index=False)