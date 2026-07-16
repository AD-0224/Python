import sys
from storage import load_passwords, save_passwords

def add_password(service):
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")

    passwords = load_passwords()

    passwords[service] = {
        "username": username,
        "password": password
    }

    save_passwords(passwords)
    print(f"Mot de passe pour {service} ajouté.")

def list_passwords():
    passwords = load_passwords()

    for service in passwords:
        print(service)

def get_account(service):
    passwords = load_passwords()

    if service in passwords:
        account = passwords[service]
        print("Username :", account["username"])
        print("Password :", account["password"])
    else:
        print("Compte introuvable")

def delete_account(service):
    passwords = load_passwords()

    if service in passwords:
        del passwords[service]
        save_passwords(passwords) 
        print(f"Compte {service} supprimé.")
    else:
        print("Compte introuvable")

def update_account(service):
    passwords = load_passwords()

    if service in passwords:
        account = passwords[service]
        new_password = input("Nouveau mot de passe :")
        account["password"] = new_password 

        save_passwords(passwords)
        print(f"Compte {service} mis à jour.")
    else:
        print("Compte introuvable")


if len(sys.argv) < 2:
    print("Usage : python3 main.py <commande>")
    exit()

command = sys.argv[1]

if command == "add":
    service = sys.argv[2]
    add_password(service)

elif command == "list":
    list_passwords()

elif command == "get":
    service = sys.argv[2]
    get_account(service)

elif command == "delete":
    service = sys.argv[2]
    delete_account(service)

elif command == "update":
    service = sys.argv[2]
    update_account(service)

else:
    print("Commande inconnue")

