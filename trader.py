import alpaca_trade_api as tradeapi
import os
import re

class tradingBot():
    def __init__(self):
        # setup alpaca api
        self.key = os.environ['ALPACA_KEY']
        self.secret = os.environ['ALPACA_SKEY']
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)

        # pick stock to trade (only one for this alg)
        self.symbol = 'IVV'

        # initially no order is being processed 
        self.current_order = None

        # get last traded price        
        closed_orders = self.api.list_orders(status='closed')
        last_order = str(closed_orders[-1])
        last_price = re.search('filled_avg_price(.+?),',last_order)
        last_price = re.split('\s', last_price.group())
        last_price = re.sub("[\',]", "", last_price[1])
        last_price = float(last_price)
        print(last_price)

        # try to set position if there is one, if not, set to 0
        try:
            self.position = int(self.api.get_position(self.symbol).qty)
        except:
            self.position = 0
        
        # assume initally that target = position
        self.target = self.position

    def get_current_price(self):
        symbol_bars = self.api.get_barset(self.symbol, 'minute', 1).df.iloc[0]
        return symbol_bars[self.symbol]['close']
