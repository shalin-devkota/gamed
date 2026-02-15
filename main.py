import argparse

BANNER = r"""
   ____    _    __  __ _____ ____  
  / ___|  / \  |  \/  | ____|  _ \ 
 | |  _  / _ \ | |\/| |  _| | | | |
 | |_| |/ ___ \| |  | | |___| |_| |
  \____/_/   \_\_|  |_|_____|____/ 

              G A M E D
         (gamedamon CLI tool)
"""

def main():
    parser = argparse.ArgumentParser(
        description="GAMED - Gamedamon CLI Tool",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "-b", "--bin",
        type=str,
        help="Include binary path here"
    )

    parser.add_argument(
        "-c", "--config",
        type=str,
        help="Include config path here"
    )
    
    args = parser.parse_args()

    if not any(vars(args).values()):
        print(BANNER)
        print("Available Commands:")
        print("  -b, --bin     Include binary path here")
        print("  -c, --config  Include config path here")
        return

    print("\nParsed Values:")
    print(f"  Binary path : {args.bin}")
    print(f"  Config path : {args.config}")

if __name__ == "__main__":
    main()
