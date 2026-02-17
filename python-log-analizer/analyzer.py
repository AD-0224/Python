import sys 
import re #module d'expressions reguliere

if len(sys.argv) < 2:
    print("Usage: python3 log_analyzer.py <logfile>")
    sys.exit(1)
logfile = sys.argv[1]
levels = {}

try:
    with open(logfile, "r") as f:
        for line in f:
            level = line.strip() #strip enleve les espaces en debut et fin de ligne
            if not line:
                continue #passe a la ligne suivante
            # match = re.search(r"\b[A-Z]{2,}\b", line) #\b borne et de fin mot en maj min 2 lettres
            matches = re.findall(r"\b[A-Z]{2,}\b", line) #re.findall(pattern, string)
            for level in matches:
                levels[level] = levels.get(level, 0) + 1 #dictionnaire vide au debut recupere la valeur actuelle si elle existe sinon 0 et le +1 incrementat° simple

    print("-----Résumé-----")
    for lvl, count in levels.items(): #paire clé valeur
        print(f"{lvl}: {count}")

except FileNotFoundError:
    print("Fichier introuvable")