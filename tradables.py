# a stock object that is an abstraction for the stock currently being traded
class stock():
    # might want to add attributes such as volume, volatility etc. when strategy is improved
    # why we getting an attribute error here?
    def __init__(trading_symbol, self):
        self.symbol = trading_symbol

    # method to get the current price
    # note: trader is an argument since it is needed to access the api
    def get_current_price(trader, self):
        symbol_bars = trader.api.get_barset(self.symbol, 'minute', 1).df.iloc[0]
        current_price = symbol_bars[self.symbol]['close']
        return current_price
