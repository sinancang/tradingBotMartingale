import alpaca_trade_api as tradeapi


class Martingale(object):
    def __init__(self):
        self.key = 'PKE4657HP93I3P0I3IOF'
        self.secret = '3xye9Z06TRu7BZP26Zyppk2Uw2TEVWLuDOFzede9'
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)
        self.symbol = 'IVV'
        self.current_order = None
        self.last_price = 1

        try:
            self.position = int(self.api.get_position(self.symbol).qty)
        except:
            self.position = 0
    
    # submits orders until position reaches target
    def submit_order(self, target):
        if self.current_order is not none:
            self.api.cancel_order(self.current_order.id)
        
        delta = target - self.position
        
        # if position is at the target, do nothing
        if delta == 0:
            return

        # otherwise do something
        print(f'Processing the order for {target} shares')
        
        # if position is positive, target > position. we need to buy
        if delta > 0:
            buy_quantity = delta
            print(f'Buying {buy_quantity} shares')
            self.current_order = self.api.submit_order(self.symbol,buy_quantity,'buy','market','day')
        
        # if position is negative, target < position, we need to sell
        elif delta < 0:
            sell_quantity = abs(delta)
            print(f'Selling {sell_quantity} shares')
            self.current_order = self.api.submit_order(self.symbol,sell_quantity,'sell','market','day')
    
    # analyse today's data to determine target
    def analyse_data(self):
        # fetch price of last buy
        # fetch current market price
        # calculate percent change
        # if there has been a decrease, increase target
        # if there has been an increase, decrease target


if __name__ == '__main__':
    t = Martingale()
    target = analyse_data
    t.submit_order(target)
