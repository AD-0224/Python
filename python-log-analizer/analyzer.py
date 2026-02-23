import re #module d'expressions reguliere

VALID_LEVELS = {"INFO","WARNING", "ERROR", "DEBUG", "CRITICAL"}
def analyze_file(filepath):
    levels = {}

    with open(filepath, "r") as f:
        for line in f:
            matches = re.findall(r"\b[a-zA-Z]{2,}\b", line) #re.findall(pattern, string)
            for word in matches:
                word = word.upper()
                if word in VALID_LEVELS:
                    levels[word] = levels.get(word, 0) + 1 #dictionnaire vide au debut recupere la valeur actuelle si elle existe sinon 0 et le +1 incrementat° simple
    return levels
