import pandas as pd
import pandas_datareader.data as web
import datetime as dt
i = 0

pd.options.mode.chained_assignment = None
port = pd.read_csv('tradingBot/test_stock.csv')

# Only part needed for trade bot is functions for buy and sell
fifty_mma = [1250, 662, 134, 400]
hundred_mma = [1277, 602, 172, 391]

port['50ma'] = fifty_mma
port['100ma'] = hundred_mma


# hundred_days = dt.timedelta(100)
# fifty_days = dt.timedelta(50)
# end = dt.datetime.now()
# start = end - hundred_days
# max_amount = 1000.0

# for each in port['stock']:
#     df = web.DataReader(each, 'yahoo', start, end)['Adj Close']
#     df = df.drop(columns=['Date'])
#     port['hundred_mma'][i] = df.mean()
#     df = df.tail(50)
#     port['fifty_mma'][i] = df.mean()
#     i += 1

print("\n\n\n")
print(port)
print("\n\n")




def buy_stock(port):
    which_index = 0
    for each in port['100ma']:
        if each * 1.05 <= port['50ma'][which_index]:
            #WILL BUY!
            port['live_price'][which_index] = 0
        which_index += 1
    return port



# port = buy_stock(port)

def sell_stock(port):
    which_index = 0
    for each in port['50ma']:
        if each * 1.05 <= port['100ma'][which_index]:
            #WILL SELL!
            port['live_price'][which_index] = 0
        which_index += 1
    return port


port = sell_stock(port)

print("\n\n This is the manipulated one: \n\n")
print(port)
