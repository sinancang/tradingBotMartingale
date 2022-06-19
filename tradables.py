from logger import log

# a stock object that is an abstraction for the stock currently being traded
class stock():
    def __init__(self):
        # get user input & create stock object accordingly
        log(("What should we trade today? "))
        self.symbol = input()
        log(f"Today, we're trading {self.symbol}, good choice!")

    # not sure if method works currently
    def get_current_price(self, trader):
        symbol_bars = trader.api.get_barset(self.symbol, 'minute', 1).df.iloc[0]
        current_price = symbol_bars[self.symbol]['close']
        return current_price
