from abc import ABC, abstractmethod, abstractproperty
import platform


class BaseGameServer(ABC):
    SUPPORTED_PLATFORMS = ["windows", "linux"]

    def __init__(self, name, binary_path, config_path, process=None):
        self.name = name
        self.binary_path = binary_path
        self.config_path = config_path
        self.process = process

    @abstractmethod
    def setup_environment(self):

        if platform.system().lower() not in self.SUPPORTED_PLATFORMS:
            raise EnvironmentError(f"Unsupported platform: {platform.system()}")
        self.platform = platform.system().lower()
        return self.platform

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
