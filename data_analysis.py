# analyse data to determine target

# compares current price to last price of symbol
# if there has been a percent change, re-calculates target & returns 1
# otherwise, returns 0

def calculate_price_change(trader):
    print(f"Our last trade of {trader.symbol} was of price {trader.last_price}")

    current_price = trader.get_current_price
    print(f"This stock's current price is {current_price}")
    
    percent_change = (last_trade.price / trader.last_price) - 1
    print(f"Percent change is {percent_change}%")

    if percent_change == 0.0:
        print("No percent change in price of stock occurred, target remains the same.")
        return 0

    past_target = trader.target

    # if there has been a decrease, increase target to buy more
    if (percent_change < 0):
        trader.target += percent_change*2
        price_change = "decrease"

        # if there has been an increase, decrease target
    elif (percent_change > 0):
        trader.target -= percent_change*2

    print(f"There has been a {price_change} in price.")
    print(f"Changed target from {past_target} to {trader.target}")
    return 1
