import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password) 

# récupère le sel dans le hash et on vérifie que le mdp donné correspond
# bcypt envoie des bytes et pas des strings !! ET hashed contient également le sel le resultat et la formule de calcule

def save_master_password(password):
    hashed = hash_password(password)
    with open("master.hash", "wb") as file:
        file.write(hashed)

def check_master_password(password):
      with open("master.hash", "rb") as file:
        hashed = file.read()
      return verify_password(password, hashed)

# save_master_password("bonjour123")
# print(check_master_password("bonjour123"))
# print(check_master_password("mauvais"))