A trading bot that uses the martingale strategy to periodically market buy/sell stocks via the alpaca api
If there has been a loss, the algorithm buys,
If there has been a win, the algorithm sells.


issues:
- strategy optimization required
- do not attempt another order before the current order is filled


It still isn't perfect but to run it, run martingale.py
