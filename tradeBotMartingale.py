import alpaca_trade_api as tradeapi


class Martingale(object):
    def __init__(self):
        # setup the environment
        self.key = 'PKE4657HP93I3P0I3IOF'
        self.secret = '3xye9Z06TRu7BZP26Zyppk2Uw2TEVWLuDOFzede9'
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)
        self.symbol = 'IVV'
        self.current_order = None
        self.target = 1
        
        # get up-to-date price for symbol
        symbol_bars = self.api.get_barset(self.symbol, 'minute', 1).df.iloc[0]
        self.last_price = symbol_bars[self.symbol]['close']
        
        # try to set position if there is one, if not, set to 0
        try:
            self.position = int(self.api.get_position(self.symbol).qty)
        except:
            self.position = 0
    
    # submits order for position to reach target
    def submit_order(self, target):
        if self.current_order is not None:
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
            self.current_order = self.api.submit_order(
                    symbol=self.symbol,
                    qty=buy_quantity,
                    side='buy',
                    type='market',
                    time_in_force='day')
            
            # update last price for use later
            self.last_price = self.api.get_last_trade(self.symbol)

        # if position is negative, target < position, we need to sell
        elif delta < 0:
            sell_quantity = abs(delta)
            print(f'Selling {sell_quantity} shares')
            self.current_order = self.api.submit_order(
                    symbol=self.symbol,
                    qty=sell_quantity,
                    side='sell',
                    type='market',
                    time_in_force='day')
            
            # update last price for use later
            self.last_price = self.api.get_last_trade(self.symbol)

    # analyse today's data to determine target
    def analyse_data(self):
        # compare current last trade to the last trade when an order was placed
        last_trade = self.api.get_last_trade(self.symbol)
        percent_change = 1 - (last_trade / self.last_price)
        
        print("Analysing data...")

        # if there has been a decrease, increase target to buy more
        if (percent_change < 1):
            print("There has been a decrease, buy more!")
            self.target += percent_change*2 
        
        # if there has been an increase, decrease target
        elif (percent_change > 1):
            print("There has been an increase, sell some!")
            self.target -= percent_change*2
        
        else:
            print("No percent change in price of stock occurred, stay put.")

if __name__ == '__main__':
    t = Martingale()
    clock = t.api.get_clock()
    if clock.is_open:
        print("Market is open! Let's try and trade.")
        t.analyse_data()
        t.submit_order(t.target)
