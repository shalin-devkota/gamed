import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description="GAMED - Gamedamon CLI Tool",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("-c", "--config", type=str, help="Path to the config JSON file")

    parser.add_argument("-g", "--game", type=str, help="Name of the game to run")

    parser.add_argument(
        "-se",
        "--setup-environment",
        action="store_true",
        help="Initial environment setup",
    )

    return parser
