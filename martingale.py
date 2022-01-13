# python lib imports
import time

# local module imports
import trader
from data_analysis import calculate_price_change
from submit_order import submit_order

if __name__ == '__main__':
    print("Hello and welcome to tradingBotMartingale!")
    print("Today we'll be using the martingale strategy which is a rather simple one:") 
    print("After buying, if there is a price decreases, we buy!")
    print("If there is a price increases, we sell!")
    t = trader.tradingBot()
    print(f"The trader bot is set up to trade {t.symbol} and will trade using the alpaca tradeapi.")
    clock = t.api.get_clock()
    if True:
        print("The market is open! Let's try and trade.")
        print(f"We start off the day with {t.position} share of {t.symbol}")
        i = 0
        while True and i < 10:
            print("Analysing data...")
            if calculate_price_change(t) == 1:
                print("Submitting order...")
                submit_order(t)
 #               t.listen_for_updates()  doesn't work yet
            i += 1
            while t.current_order != None:
                print('waiting for order to be filled...')
                time.sleep(1)
    else:
        print("The market is currently closed, come back later!")
