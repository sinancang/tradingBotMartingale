import alpaca_trade_api as tradeapi
import tradables

import os

# as this is a trade API it should only be used to place orders
class AlpacaAPI():
    def __init__(self):
        self.key = os.environ['APCA_API_KEY_ID']
        self.secret = os.environ['APCA_API_SECRET_KEY']
        self.alpaca_endpoint = os.environ['APCA_API_BASE_URL']

        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)

        self.instrument = tradables.stock()

        self.current_order = None

    def get_current_price(self):
        # I need to get a better grasp of get_barset
        # might want to set the time interval to something less than a minute
        symbol_bars = self.api.get_barset(self.symbol, 'minute', 1).df.iloc[0]
        current_price = symbol_bars[self.symbol]['close']

        return current_price
