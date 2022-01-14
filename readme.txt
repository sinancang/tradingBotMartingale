A trading bot that uses the martingale strategy to periodically market buy/sell stocks via the alpaca api
If there has been a loss, the algorithm buys,
If there has been a win, the algorithm sells.


issues:
	difficult:
		- strategy optimization required
		- allow for generalization such as using other api's, other types of buys and trading objects(shorts, longs, options etc.)
	
	medium:
		- why is the stock object being initialized as a str?
		- how should submit_order update last_price? get avg filled price for stock OR using stock.get_current_price. which is more accurate?
		- simplify regex expression

	low-hanging-fruit:
		- cancel order if listening takes too long
		- take user input for symbol

To run, set up APCA_API_KEY_ID, APCA_API_SECRET_KEY and APCA_API_BASE_URL environment variables, then type "python martingale.py" on the command line.
