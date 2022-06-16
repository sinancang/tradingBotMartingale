import alpaca_trade_api as tradeapi
import os

class AlpacaAPI():
    def __init__(self, tradable):
        # setup alpaca api
        self.key = os.environ['APCA_API_KEY_ID']
        self.secret = os.environ['APCA_API_SECRET_KEY']
        self.alpaca_endpoint = os.environ['APCA_API_BASE_URL']
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)

        # initially no order is being processed
        self.current_order = None