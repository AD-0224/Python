import re #regular expression module

VALID_LEVELS = {"INFO","WARNING", "ERROR", "DEBUG", "CRITICAL"}
def analyze_file(filepath):
    levels = {}

    with open(filepath, "r") as f:
        for line in f:
            matches = re.findall(r"\b[a-zA-Z]{2,}\b", line) #re.findall(pattern, string)
            for word in matches:
                word = word.upper()
                if word in VALID_LEVELS:
                    levels[word] = levels.get(word, 0) + 1 
                    #empty dictionary at the beginning, retrieves the current value if it exists, otherwise 0 and +1 simple increment
    return levels
