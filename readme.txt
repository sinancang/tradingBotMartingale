DISCLAIMER: NOT READY FOR DEPLOYMENT

!! Currently a migration to a more scalable and decoupled system is in progress... !!

A trading bot that uses the martingale strategy to periodically market buy/sell stocks via the alpaca api
If there has been a loss, the algorithm buys,
If there has been a win, the algorithm sells.

To run, set up APCA_API_KEY_ID, APCA_API_SECRET_KEY and APCA_API_BASE_URL environment variables, then type "python martingale.py" on the command line.
