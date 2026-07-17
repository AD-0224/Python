import sys
import argparse
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


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add")
list_parser = subparsers.add_parser("list")
get_parser = subparsers.add_parser("get")
update_parser = subparsers.add_parser("update")
delete_parser = subparsers.add_parser("delete")

add_parser.add_argument("--service", required=True)
get_parser.add_argument("--service", required=True)
update_parser.add_argument("--service", required=True)
delete_parser.add_argument("--service", required=True)

args = parser.parse_args()

if args.command == "add":
    add_password(args.service)

elif args.command == "list":
    list_passwords()

elif args.command == "get":
    get_account(args.service)

elif args.command == "delete":
    delete_account(args.service)

elif args.command == "update":
    update_account(args.service)

