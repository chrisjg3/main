import time
import pandas as pd
from yahoo_fin import stock_info as si


def change_port(port):
    active = ""
    found_stock = False
    while active.lower() != "yes" and active.lower() != "no":
        active = input("Do you want to sell or buy any of your currently held stocks? \n yes or no: ")
        print("\n")
    if active.lower() == "no":
        print("Okay, you have chosen to not change your portfolio \n")
    while active.lower() == "yes":
        whichstock = input("\n Type the abbreviation of the stock you would like to buy or sell. \n Stock Abbreviation: ")

        # This first checks if the stock has been added in the past
        for each in port['stock']:  
            if each == whichstock:
                found_stock = True
        
        # This adds the stock abbrevaition to the csv, if it as never been added in the past.
        if found_stock == False: 
            to_add = pd.DataFrame(
            {'stock': [whichstock], 'live_price': [si.get_live_price(whichstock)], 'quantity': [0], 'value_now': [0], 'current_invest': [0],
            'loss/gain': [0]})
            port = port.append(to_add, ignore_index=True)

        # This is where buying/selling and quantity are asked and chosen.  The code jumps here if the stock was already in csv
        buy_or_sell = input("Do you wish to buy or sell the stock? ")
        quantity = input("Quantity: ")
        buyprice = si.get_live_price(whichstock.lower())
        try:
            quantity = int(quantity)
        except:
            print("Must enter an integer.  It has been set to 1.")
            quantity = 1
            time.sleep(1)

        # I find the index usin .index.item where the entered stock matches a row then...
        # Make an equation to change the current_invest and quanitity.
        # So that complicated equation below is really port['current_invest][row num] = port[current_invest now][index] - P * Q
        # It is the same for the next equation with quanity AND the equations under sell.
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

        # This line is asking to begin loop again:
        active = input("\n Do you want to sell or buy any additional of your current stocks? (yes or no) ") 


    port = port.round(0)
    print("Updated Portfolio: \n \n")
    print(port)
    return port
