import sys
from src.cli.parser import create_parser
from src.cli.validators import (
    validate_game,
    validate_config_path,
)
from src.integrations.minecraft.minecraft import MinecraftGameServer
from src.db.db_init import initialize_database
import json

registry = {
    "minecraft": MinecraftGameServer,
}


def main():
    initialize_database()
    parser = create_parser()
    args = parser.parse_args()

    try:
        validate_game(args.game, registry)
        validate_config_path(args.config)
    except ValueError as e:
        print(f"Error occured: {e}")
        sys.exit(1)

    print("Parsed Values:")
    print(f"  Game       : {args.game}")
    print(f"  Config path: {args.config}")

    GameServer = registry[args.game.lower()]
    server = GameServer(
        name=args.game,
        config_path=args.config,
    )
    if args.setup_environment:
        server.setup_environment()
    else:
        server.start_server()


if __name__ == "__main__":
    main()
