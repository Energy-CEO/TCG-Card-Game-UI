import abc


class ReceiverController(abc.ABC):
    @abc.abstractmethod
    def requestToInjectSocketClient(self, socketClient):
        pass

    @abc.abstractmethod
    def requestToReceiveCommand(self):
        pass


