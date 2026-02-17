import sys

def get_filepath(): #recup chemin fichier
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <logfile>")
        sys.exit(1)
    return sys.argv[1]