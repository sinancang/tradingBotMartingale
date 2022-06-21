import datetime

import alpaca_trade_api as tradeapi
import websocket

import Alpaca_credentials
from utils.logger import log

# as this is a trade API it should only be used to place orders
class AlpacaAPI():
    def __init__(self):
        self.key = Alpaca_credentials.public_key
        self.secret = Alpaca_credentials.secret_key
        self.alpaca_endpoint = Alpaca_credentials.endpoint
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)
        self.current_order = None

    def connect(self):
        log("Connecting...")
        ws = websocket.create_connection("wss://stream.data.alpaca.markets/v2/iex")
        result = ws.recv()
        log(f"<{result}")
        self.ws = ws
        # TODO: Handle failed connection

    def authenticate(self):
        log("Logging in...")
        logon = {"action": "auth", "key": self.key, "secret": self.secret}
        self.ws.send(logon)
        log(f">{logon}")

        result = self.ws.recv()
        log(f"<{result}")
        # TODO: Handle failed authentication

    def subscribe(self, instrument_set):
        # TODO: Implement
        pass

    def listen(self):
        while datetime.datetime.now().hour < 17 and datetime.datetime.now().hour > 9:
            log(f"<{self.ws.recv()}")