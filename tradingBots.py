import alpaca_trade_api as tradeapi
import os
import re

class tradingBot():
    def __init__(self, tradable):
        # setup alpaca api
        self.key = os.environ['APCA_API_KEY_ID']
        self.secret = os.environ['APCA_API_SECRET_KEY']
        self.alpaca_endpoint = os.environ['APCA_API_BASE_URL']
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)

        # initially no order is being processed 
        self.current_order = None

        self.trading = tradable

        # get last order price for tradable
        closed_orders = self.api.list_orders(status='closed')
        last_order = str(closed_orders[-1])
        x = last_order.split("\n")

        num = float((nums_from_string.get_nums(x[9])[0]))

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
