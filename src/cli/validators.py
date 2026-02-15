import os
import json

def validate_game(game_name: str, registry: dict):
    if game_name.lower() not in registry:
        raise ValueError(
            f"Game '{game_name}' is not supported. "
            f"Available games: {', '.join(registry.keys())}"
        )

def validate_binary_path(path: str):
    if not os.path.isfile(path):
        raise ValueError(f"Binary path '{path}' does not exist or is not a file.")

def validate_config_path(path: str):
    if not os.path.isfile(path):
        raise ValueError(f"Config path '{path}' does not exist.")

    if not path.endswith(".json"):
        raise ValueError("Config file must be a JSON file (.json).")

    try:
        with open(path, "r") as f:
            json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Config file is not valid JSON.")
