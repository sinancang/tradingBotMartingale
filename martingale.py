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
    if clock.is_open:
        print("The market is open! Let's try and trade.")
        print(f"We start off the day with 1 share of {t.symbol}")
        submit_order(t)
        trader.target = 1
        i = 0
        while clock.is_open and i < 10:
            print("Analysing data...")
            time.sleep(3)
            if calculate_price_change(t) == 1:
                submit_order(t)
            i += 1
