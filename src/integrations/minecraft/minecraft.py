from src.base.baseGameServer import BaseGameServer
import json
import subprocess
from .preflight_checks import system_has_java
from .environments.linux import setup_linux_environment
from .environments.windows import setup_windows_envrionment
import os


class MinecraftGameServer(BaseGameServer):
    START_TEMPLATE = "java -Xmx{max_memory}G -Xms{min_memory}G -jar {jar} nogui"

    def __init__(self, name, config_path):
        super().__init__(name=name, config_path=config_path)
        with open(self.config_path, "r") as f:
            config = json.load(f)
        self.binary_path = config.get("binary_path", None)
        if not self.binary_path:
            raise ValueError(
                "Config must include 'binary_path' for the Minecraft server jar."
            )
        self.max_memory = config.get("max_memory", 2)
        self.min_memory = config.get("min_memory", 1)
        instance_name = config.get(
            "instance_name", None
        )  # Todo : handle none later, maybe auto gen a instance name.
        self.directory = os.path.join(
            self.base_game_directory, instance_name
        )  # TODO: handle none here too

    @property
    def start_string(self):
        return self.START_TEMPLATE.format(
            max_memory=self.max_memory, min_memory=self.min_memory, jar=self.binary_path
        )

    def run_preflight(self):
        if not system_has_java():
            raise EnvironmentError("Java is not installed or not found in PATH.")
        return True

    def setup_environment(self):
        platform = super().setup_environment()
        if platform == "windows":
            setup_windows_envrionment()
        else:
            setup_linux_environment()

    def setup_game_directory(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            print(f"Created game directory at: {self.directory}")
        else:
            print(f"Game directory already exists at: {self.directory}")

    def start_server(self):
        self.setup_game_directory()
        if self.run_preflight():

            self.process = subprocess.Popen(
                self.start_string,
                shell=True,
                cwd=os.path.join(self.directory),
            )
            print(f"Started Minecraft server with PID: {self.process.pid}")
            return self.process
        else:
            print("Preflight checks failed. Server not started.")
            return None

    def stop_server(self):
        if not self.process:
            print("Server is not running.")
            return
        self.process.terminate()

    def restart_server(self):
        print(f"Restarting Minecraft server: {self.name}")
        self.stop_server()
        self.start_server()
