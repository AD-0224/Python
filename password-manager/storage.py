import json 
import os

FILE = "passwords.json"

def load_passwords():
    if not os.path.exists(FILE): 
        return {}
    
    with open(FILE, "r") as file:
        return json.load(file) #Convert JSON data to Python object
    
def save_passwords(passwords):
        with open(FILE, "w") as file:
            json.dump(passwords, file, indent=4) #Convert Python object to JSON