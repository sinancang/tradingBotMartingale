# submits a order for the target to be equal to the position
def submit_order(trader):
    if trader.current_order is not None:
        trader.api.cancel_order(self.current_order.id)

    delta = trader.target - trader.position

    print(f'Processing the order for {delta} shares')

    # if position is positive, target > position. we need to buy
    if delta > 0:
        buy_quantity = delta
        print(f'Buying {buy_quantity} shares')
        trader.current_order = trader.api.submit_order(
            symbol=trader.symbol,
            qty=buy_quantity,
            side='buy',
            type='market',
            time_in_force='day')

    # if position is negative, target < position, we need to sell
    elif delta < 0:
        sell_quantity = abs(delta)
        print(f'Selling {sell_quantity} shares')
        trader.current_order = trader.api.submit_order(
            symbol=trader.symbol,
            qty=sell_quantity,
            side='sell',
            type='market',
            time_in_force='day')

    # update last price for use later
    trader.last_price = trader.api.get_last_trade(trader.symbol).price
