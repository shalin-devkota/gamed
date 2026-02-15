from base.baseGameServer import BaseGameServer
import json
import subprocess


class MinecraftGameServer(BaseGameServer):
    START_TEMPLATE = "java -Xmx{ max_memory}G -Xms{min_memory}G -jar {jar} nogui"

    def __init__(self, name, binary_path, config_path, max_memory, min_memory):
        super().__init__()
        with open(self.config_path, "r") as f:
            config = json.load(f)

        max_memory = config.get("max_memory", 2)
        min_memory = config.get("min_memory", 1)

    @property
    def start_string(self):
        self.START_TEMPLATE.format(
            max_memory=self.max_memory, min_memory=self.min_memory, jar=self.binary_path
        )

    def start_server(self):
        self.process = subprocess.Popen(self.start_string, shell=True)
        return self.process

    def stop_server(self):
        if not self.process:
            print("Server is not running.")
            return
        self.process.terminate()

    def restart_server(self):
        print(f"Restarting Minecraft server: {self.name}")
        self.stop_server()
        self.start_server()
