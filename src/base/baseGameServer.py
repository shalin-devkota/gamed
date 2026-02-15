from abc import ABC, abstractmethod, abstractproperty
import platform
import os
import json


class BaseGameServer(ABC):
    SUPPORTED_PLATFORMS = ["windows", "linux"]

    def __init__(self, name, config_path, process=None):
        self.name = name

        self.config_path = config_path
        self.process = process
        self.user_home = os.path.expanduser("~")

        with open("config.json", "r") as f:
            global_config = json.load(f)
            base_directory = global_config.get("base_game_directory", self.user_home)

            base_game_directory = os.path.join(base_directory, self.name)
            self.base_game_directory = base_game_directory

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
