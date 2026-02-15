from abc import ABC, abstractmethod, abstractproperty


class BaseGameServer(ABC):
    def __init__(self, name, binary_path, config_path, process=None):
        self.name = name
        self.binary_path = binary_path
        self.config_path = config_path
        self.process = process

    @abstractmethod
    def start_server(self):
        pass

    @abstractmethod
    def stop_server(self):
        pass

    @abstractmethod
    def restart_server(self):
        self.stop_server()
        self.start_server()

    @property
    @abstractmethod
    def start_string(self):
        pass
