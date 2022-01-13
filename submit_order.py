# submits a order for the target to be equal to the position
def submit_order(trader):
    # delta is the distance of position to target
    delta = trader.target - trader.position
    print(f'Processing the order for {delta} shares')

    # if delta is positive, target > position. we need to buy
    if delta > 0:
        print(f'Buying {delta} shares')
        order_type = 'buy'

    # if delta is negative, target < position, we need to sell
    elif delta < 0:
        delta = abs(delta)
        print(f'Selling {delta} shares')
        order_type = 'sell'
    
    trader.current_order = submit_order_helper(order_type, delta)
   
    # update last price for use later
    trader.last_price = trader.current_order.filled_avg_price

def submit_order_helper(order_type, quantity):
    trader.current_order = trader.api.submit_order(
        symbol=trader.symbol,
        qty=delta,
        side=order_type,
        type='market',
        time_in_force='day')
