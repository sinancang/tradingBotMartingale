from .instrument import Instrument

class Stock(Instrument):
    type = 'stock'

    def __init__(self, symbol):
        self.symbol = symbol