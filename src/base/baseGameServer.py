from abc import ABC, abstractmethod
import platform
import os
import json
from src.db.db_gameserver import get_or_create_gameserver


class BaseGameServer(ABC):
    SUPPORTED_PLATFORMS = ["windows", "linux"]

    def __init__(self, name, config_path, process=None):
        self.name = name

        self.config_path = config_path
        self.process = process
        self.user_home = os.path.expanduser("~")

        # global config handler
        with open("config.json", "r") as f:
            global_config = json.load(f)
            base_directory = global_config.get("base_game_directory", self.user_home)

            base_game_directory = os.path.join(base_directory, self.name)
            self.base_game_directory = base_game_directory

        # instance specific config handler
        with open(self.config_path, "r") as f:
            instance_config = json.load(f)
            self.instance_name = instance_config.get("instance_name", None)
            self.binary_path = instance_config.get("binary_path", None)
            # Todo: add better validation. prolly pydnatic will be good
            if not self.instance_name:
                raise ValueError(
                    "Config must include 'instance_name' for the server instance."
                )
            self.directory = os.path.join(self.base_game_directory, self.instance_name)

    def get_or_create_gameserver(self):
        return get_or_create_gameserver(
            game_name=self.name,
            instance_name=self.instance_name,
            directory=self.directory,
            config_path=self.config_path,
        )

    def start_server(self):
        gameserver = self.get_or_create_gameserver()
        self._start_server(gameserver)

    @abstractmethod
    def setup_environment(self):
        if platform.system().lower() not in self.SUPPORTED_PLATFORMS:
            raise EnvironmentError(f"Unsupported platform: {platform.system()}")
        self.platform = platform.system().lower()
        return self.platform

    @abstractmethod
    def _start_server(self, gameserver):
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
