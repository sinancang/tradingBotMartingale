# python lib imports
import time

# local module imports
import tradables, API_old
from data_analysis import calculate_price_change

if __name__ == '__main__':
    print("Hello and welcome to tradingBotMartingale!")
    print("Today we'll be using the martingale strategy which is a rather simple one:") 
    print("After buying, if there is a price decreases, we buy!")
    print("If there is a price increases, we sell!")
  
    # initialize stock object
    trading_object = tradables.stock()

    # initialize tradingbot 
    trading_entity = tradingBots.tradingAlpaca(trading_object)
    print(f"The trader bot is set up to trade {trading_object.symbol} and will trade using the alpaca tradeapi.")
    
    # check if market is open
    clock = trading_entity.api.get_clock()
    if clock.is_open():
        print("The market is open! Let's try and trade.")
        print(f"We start off the day with {trading_entity.position} share of {trading_object.symbol}")

        # attempt to trade 10 times and while market is open
        i = 0
        while clock.is_open() and i < 10:
            print("Analysing data...")

            #
            if calculate_price_change(trading_entity) == 1:
                print("Submitting order...")
                trading_entity.submit_order()
                print('waiting for order to be filled...')
                trading_entity.listen_for_updates()
                i += 1
    else:
        print("The market is currently closed, come back later!")
