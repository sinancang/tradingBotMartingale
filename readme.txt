A trading bot that uses the martingale strategy to periodically market buy/sell stocks via the alpaca api
If there has been a loss, the algorithm buys,
If there has been a win, the algorithm sells.


issues:
- strategy optimization required

To run, set up APCA_API_KEY_ID, APCA_API_SECRET_KEY and APCA_API_BASE_URL environment variables, then type "python martingale.py" on the command line.
