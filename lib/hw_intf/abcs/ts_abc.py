import abc

class TS_ABC():
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def get_temp(self):
        pass
