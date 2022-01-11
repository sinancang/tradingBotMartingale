A simple trading bot that uses the martingale strategy by checking the past time-frame to see if there has been a win or a loss. 
If there has been a loss, the algorithm increases the bet, if there has been a win, the algorithm sells an amount of the stock.


issues:
- need to convert variable trade to float in analyze_data
- program needs more scalability.
- the strategy is not optimal
- code smells: submitting orders can be done through a single helper method
