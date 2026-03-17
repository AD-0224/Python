import sys

def get_filepath(): #retrieve file path
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <logfile>")
        sys.exit(1)
    return sys.argv[1]