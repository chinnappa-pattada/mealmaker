import abc

class HE_ABC():
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def heat_on(self):
        pass
    @abc.abstractmethod
    def heat_off(self):
        pass
