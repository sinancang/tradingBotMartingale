import Alpaca_API as alpaca
from utils.logger import log
import instruments

def main():
    log("Welcome to AI trader")
    API = alpaca.AlpacaAPI()
    API.connect()
    API.authenticate()

    instrument_set = set()
    inst1 = instruments.Stock('AMD')
    instrument_set.add(inst1)

    API.subscribe(instrument_set)
    API.listen()

if __name__ == '__main__':
    main()