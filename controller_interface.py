from abc import abstractmethod

from model import Model

class ControllerBase():
    @abstractmethod
    def changePageTo(self,index):
        pass
    @abstractmethod
    def exitTheApp(self):
        pass

    @abstractmethod
    def setup_signal_handler(self, worker):
        pass

    @abstractmethod
    def chatwith(self, indivtochat):
        pass

    @abstractmethod
    def getmodel(self) -> Model:
        pass