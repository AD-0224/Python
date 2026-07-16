import json 
import os

FILE = "passwords.json"

def load_passwords():
    if not os.path.exists(FILE): 
        return{}
    
    with open(FILE, "r") as file:
        return json.load(file) #on passe de JSON à Python
    
def save_passwords(passwords):
        with open(FILE, "w") as file:
            json.dump(passwords, file, indent=4) #on passe de python a JSON 