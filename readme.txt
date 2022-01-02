A simple trading bot that uses the martingale strategy by checking the past time-frame to see if there has been a win or a loss. 
If there has been a loss, the algorithm increases the bet, if there has been a win, the algorithm sells an amount of the stock.

need to implement:
- program must store somewhere the market price at the previous check
- program must periodically attempt to calculate target to buy or sell
	- can implement with while loop. issue is that it may be too fast resulting in a lot of unnecesary calculations. 
	  something that freezes the program for a certain period of time would solve this
- must implement analyse data function. ex: how much of the stock should be sold in the case of a 10% increase?
	- this is connected lightly to how risk tolerant we want to be. more risk tolerance means more betting when lost.
- must not hard-code key and secretkey. instead, define them as variables in bash_profile and fetch in program
	  
strategy analysis with examples:
ex: buy in at 10. %2 decrease, new price is 8. 40 dollars worth of buy (5 buys).
owning 6 shares. to make up for the losses our portfolio needs to increase in value by 4%, which is a 0.7% increase in shares.

naive assumption: an increase in price will happen. naive response: double the bet and play.
ex: buy in at 10. %2 decrease, new price: 8. 2 more buys (worth in total 16 dollars). total worth: 24. 
to make the 2 dollars back, we need a total increase of our portfolio of 8.3%, which needs 2.7% increase in the stock.

what if we multiply the size of the portfolio:
buy in at 10. 2% decrease, new price 8. 1 more buy, total worth is 16$.
to make the money back, we need a 8 percent increase in the stock, which seems more unlikely.

somehow i feel like the amount bet needs to depend on the percent increase

issues:
- program is not scalable. everything is done within a single file. increased complexity will cause messiness
- the strategy is trash haha
