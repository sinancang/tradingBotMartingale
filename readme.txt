A trading bot that uses the martingale strategy to periodically market buy/sell stocks via the alpaca api
If there has been a loss, the algorithm buys,
If there has been a win, the algorithm sells.


issues:
- need to convert variable trade to float in analyze_data
- program needs scalability.
- strategy optimization -> grid strategy
- code smells: submitting orders can be done through a single helper method
- change if statement to while loop for continuously processing, might need a sleep in there
