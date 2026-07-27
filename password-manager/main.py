import argparse
import getpass
import os

from storage import load_passwords, save_passwords
from auth import save_master_password, check_master_password
from crypto import encrypt_password, decrypt_password, derive_key, load_salt, generate_salt, save_salt
from generator import generate_password

def add_password(service, key):
    username = input("Nom d'utilisateur : ")
    choice = input("Générer un mot de passe automatiquement ? (o/n) : ")

    if choice.lower() == "o":
        password = generate_password()
        print("Mot de passe généré :", password)
    else:
        password = getpass.getpass("Mot de passe : ")

    passwords = load_passwords()
    encrypted_password = encrypt_password(password, key)
    passwords[service] = {
        "username": username,
        "password": encrypted_password.decode()
    }
    save_passwords(passwords)

    print(f"Mot de passe pour {service} ajouté.")

def list_passwords():
    passwords = load_passwords()

    for service in passwords:
        print(service)

def get_account(service, key):
    passwords = load_passwords()

    if service in passwords:
        account = passwords[service]
        print("Username :", account["username"])
        password = decrypt_password(
            account["password"].encode(),
            key
        )
        print("Password :", password)

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

def update_account(service, key):
    passwords = load_passwords()

    if service in passwords:
        account = passwords[service]
        new_password = getpass.getpass("Nouveau mot de passe : ")
        account["password"] = encrypt_password(new_password, key).decode()

        save_passwords(passwords)
        print(f"Compte {service} mis à jour.")
    else:
        print("Compte introuvable")

if not os.path.exists("master.hash"):
    print("Création du master password")

    password = getpass.getpass("Choisissez un master password : ")

    save_master_password(password)

    salt = generate_salt()
    save_salt(salt)

    print("Master password créé.")

else:
    password = getpass.getpass("Master password : ")

    if check_master_password(password):
        print("Accès autorisé.")
    else:
        print("Mot de passe incorrect.")
        exit()


if not os.path.exists("salt.bin"):
    salt = generate_salt()
    save_salt(salt)
else:
    salt = load_salt()

key = derive_key(password, salt)

key = derive_key(password, salt)
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
    add_password(args.service, key)

elif args.command == "list":
    list_passwords()

elif args.command == "get":
    get_account(args.service, key)

elif args.command == "delete":
    delete_account(args.service)

elif args.command == "update":
    update_account(args.service, key)

