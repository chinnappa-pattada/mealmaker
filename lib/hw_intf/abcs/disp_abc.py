import abc

class DISP_ABC():
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def dispense(self):
        pass
