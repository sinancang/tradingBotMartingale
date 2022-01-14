# python lib imports
import time

# local module imports
import tradables, tradingBots
from data_analysis import calculate_price_change
from submit_order import submit_order

if __name__ == '__main__':
    print("Hello and welcome to tradingBotMartingale!")
    print("Today we'll be using the martingale strategy which is a rather simple one:") 
    print("After buying, if there is a price decreases, we buy!")
    print("If there is a price increases, we sell!")
   
    # get user input & create stock object accordingly
    # currently doesn't accept user input, but it should
    print("What should we trade today?")
    trading_symbol = 'IVV'
    #trading = tradables.stock(trading_symbol)
    
    # initialize tradingbot 
    t = tradingBots.tradingBot(tradables.stock(trading_symbol))
    print(f"The trader b`ot is set up to trade {t.trading.symbol} and will trade using the alpaca tradeapi.")
    
    # check if market is open
    clock = t.api.get_clock()
    if clock.is_open:
        print("The market is open! Let's try and trade.")
        print(f"We start off the day with {t.position} share of {t.trading.symbol}")

        # attempt to trade 10 times and while market is open
        i = 0
        while clock.is_open and i < 10:
            print("Analysing data...")

            #
            if calculate_price_change(t) == 1:
                print("Submitting order...")
                submit_order(t)
            print('waiting for order to be filled...')
            t.listen_for_updates()
            i += 1
    else:
        print("The market is currently closed, come back later!")
