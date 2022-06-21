import abc

class Instrument:
    @property
    @abc.abstractmethod
    def type(self):
        raise NotImplementedError