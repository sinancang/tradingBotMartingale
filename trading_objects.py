import alpaca_trade_api as tradeapi
import os
import re

class tradingBot():
    def __init__(what_we_trading, self):
        # setup alpaca api
        self.key = os.environ['APCA_API_KEY_ID']
        self.secret = os.environ['APCA_API_SECRET_KEY']
        self.alpaca_endpoint = os.environ['APCA_API_BASE_URL']
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)

        # pick stock to trade (only one for this alg)
        self.trading = what_we_trading

        # initially no order is being processed 
        self.current_order = None

        # get last traded price of the stock we're trading
        # there's probably a more elegant regex line of code here...
        closed_orders = self.api.list_orders(symbol=self.trading.symbol,status='closed')
        last_order = str(closed_orders[-1])
        last_price = re.search('filled_avg_price(.+?),',last_order)
        last_price = re.split('\s', last_price.group())
        last_price = re.sub("[\',]", "", last_price[1])
        self.last_price = float(last_price)

        # try to set position if there is one, if not, set to 0
        try:
            self.position = float(self.api.get_position(trading.symbol).qty)
        except:
            self.position = 0
        
        # assume initally that target = position
        self.target = self.position

    def listen_for_updates(self):
        conn = tradeapi.stream2.StreamConn()
        client_order_id = self.current_order.id
        @conn.on(client_order_id)
        async def on_msg(conn, channel, data):
            print("Update for {}. Event: {}.".format(client_order_id, data['event']))
            
            # need to add additional functionality for different events such as: filled, failed, etc
            print("Order filled!")
            current_order = None

        print("Listening for updates on our order")
        conn.run(['trade_updates'])

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
