import Alpaca_API as alpaca
from logger import log

def main():
    log("Welcome to AI trader")
    API = alpaca.AlpacaAPI()

if __name__ == '__main__':
    main()