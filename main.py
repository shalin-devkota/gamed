import sys
from src.cli.parser import create_parser
from src.cli.validators import (
    validate_game,
    validate_binary_path,
    validate_config_path,
)
from src.integrations.minecraft.minecraft import MinecraftGameServer

registry = {
    "minecraft": MinecraftGameServer,
}

def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        validate_game(args.game, registry)
        validate_binary_path(args.bin)
        validate_config_path(args.config)
    except ValueError as e:
        print(f"Error occured: {e}")
        sys.exit(1)

    print("Parsed Values:")
    print(f"  Game       : {args.game}")
    print(f"  Binary path: {args.bin}")
    print(f"  Config path: {args.config}")

    GameServer = registry[args.game.lower()]
    server = GameServer(
        name=args.game,
        binary_path=args.bin,
        config_path=args.config,
    )
    if args.setup_environment:
        server.setup_environment()

    server.start_server()
    print("\nServer instance created successfully.")

if __name__ == "__main__":
    main()
