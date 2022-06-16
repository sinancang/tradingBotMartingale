from datetime import date

from API import AlpacaAPI as alpaca
from logger import log
from tradables import stock

# this file is the basis for a more scalable trading bot with replaceable and decoupled strategies and data recording


def main():
    log("Welcome to AI trader")
    trading = stock()
    curr = alpaca(trading)

    # initialize recorder and record


if __name__ == '__main__':
    main()