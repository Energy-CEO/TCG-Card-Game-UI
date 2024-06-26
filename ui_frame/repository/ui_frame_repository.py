import abc


class UiFrameRepository(abc.ABC):

    @abc.abstractmethod
    def switchFrameWithMenuName(self, menu_name):
        pass

    @abc.abstractmethod
    def registerUiFrame(self, name, newFrame):
        pass

    @abc.abstractmethod
    def saveTransmitIpcChannel(self, transmitIpcChannel):
        pass

    @abc.abstractmethod
    def saveReceiveIpcChannel(self, receiveIpcChannel):
        pass

    @abc.abstractmethod
    def saveMusicPlayIpcChannel(self, musicPlayIpcChannel):
        pass
