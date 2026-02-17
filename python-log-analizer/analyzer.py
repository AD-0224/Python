import re #module d'expressions reguliere
def analyze_file(filepath):
    levels = {}

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip() #strip enleve les espaces en debut et fin de ligne
            if not line:
                continue #passe a la ligne suivante
            # match = re.search(r"\b[A-Z]{2,}\b", line) #\b borne et de fin mot en maj min 2 lettres
            matches = re.findall(r"\b[A-Z]{2,}\b", line) #re.findall(pattern, string)
            for level in matches:
                levels[level] = levels.get(level, 0) + 1 #dictionnaire vide au debut recupere la valeur actuelle si elle existe sinon 0 et le +1 incrementat° simple
    return levels
