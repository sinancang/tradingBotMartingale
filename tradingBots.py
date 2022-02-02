import alpaca_trade_api as tradeapi
import os

class tradingAlpaca():
    def __init__(self, tradable):
        # setup alpaca api
        self.key = os.environ['APCA_API_KEY_ID']
        self.secret = os.environ['APCA_API_SECRET_KEY']
        self.alpaca_endpoint = os.environ['APCA_API_BASE_URL']
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)

        # initially no order is being processed 
        self.current_order = None

        self.trading = tradable

        # get current price of tradable
        self.last_price = self.trading.get_current_price(self)

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
            # for example: updating the last price for trader here
            print("Order filled!")
            current_order = None

        print("Listening for updates on our order")
        conn.run(['trade_updates'])


    # submits a market buy order for the target to be equal to the position
    def submit_order(self):
        # delta is the distance of position to target
        delta = self.target - self.position
        print(f'Processing the order for {delta} shares of {self.trading.symbol}')

        # if delta is positive, target > position. we need to buy
        if delta > 0:
            print(f'Buying {delta} shares')
            order_type = 'buy'

        # if delta is negative, target < position, we need to sell
        else:
            # if we don't have any shares to sell, break!
            if self.position == 0:
                print("We don't have any shares to sell!")
                break;

            delta = abs(delta)
            print(f'Selling {delta} shares')
            order_type = 'sell'

            # if we have less than we can sell, we sell what we have
            if delta > self.position:
                delta = self.position

        self.current_order = submit_order_helper(self, order_type, delta)
        
        self.last_price = trader.current_order.filled_avg_price
    
    def submit_order_helper(trader, order_type, delta):
        return trader.api.submit_order(
            symbol=trader.trading.symbol,
            qty=delta,
            side=order_type,
            type='market',
            time_in_force='day')

