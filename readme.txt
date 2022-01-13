A trading bot that uses the martingale strategy to periodically market buy/sell stocks via the alpaca api
If there has been a loss, the algorithm buys,
If there has been a win, the algorithm sells.


issues:
- strategy optimization required
- listen for updates, wait for order to be filled before attempting another

To run, type "python martingale.py" on the command line.
