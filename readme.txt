A trading bot that uses the martingale strategy to periodically market buy/sell stocks via the alpaca api
If there has been a loss, the algorithm buys,
If there has been a win, the algorithm sells.


issues:
- need to convert variable trade to float in analyze_data
- program needs more scalability.
- the strategy is not optimal
- code smells: submitting orders can be done through a single helper method
