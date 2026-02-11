# import sys

# print("Arguments recues: ")
# print(sys.argv)

# import sys 

# if len(sys.argv) < 2: #verifie les args condition si au moins 1 fichier
#     print("Usage: Python3 log_analyzer.py <logfile>")
#     sys.exit (1)
# logfile = sys.argv[1]
# try:
#     with open(logfile, "r") as f: #open ouvre un fichier | with fermeture auto
#         lines = f.readlines() #f.readlines lit tout le fichier
#         print(f"Nombre de lignes : {len(lines)}")
# except FileNotFoundError: #try et exept gestion erreur propre
#     print("Fichier introuvable")

# import sys 

# if len(sys.argv) < 2: #verifie les args condition si au moins 1 fichier
#     print("Usage: Python3 log_analyzer.py <logfile>")
#     sys.exit (1)
# logfile = sys.argv[1]

# info = 0
# Warning = 0
# error = 0

# try:
#     with open(logfile, "r") as f:
#         for line in f: #traitement en streaming lit une ligne la traite et next
#             print(line.strip())
# except FileNotFoundError:
#     print("Fichier introuvable")

import sys 

if len(sys.argv) < 2:
    print("Usage: python3 log_analyzer.py <logfile>")
    sys.exit(1)
logfile = sys.argv[1]

info = 0
warning = 0 
error = 0

try:
    with open(logfile, "r") as f:
        for line in f:
            if "INFO" in line:
                info += 1
            elif "WARNING" in line:
                warning += 1
            elif "ERROR" in line:
                error += 1
    print("----- Résumé -----")
    print(f"INFO: {info}")
    print(f"WARNING: {warning}")
    print(f"ERROR {error}")

except FileNotFoundError:
    print("Fichier introuvable")