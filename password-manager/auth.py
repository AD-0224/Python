import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password) 
# récupère le sel dans le hash et on vérifie que le mdp donné correspond

# hashed = hash_password("bonjour123")

# print("Hash :", hashed)
# print("Correct :", verify_password("bonjour123", hashed))
# print("Incorrect :", verify_password("bonjour 123", hashed))
# print("Incorrect :", verify_password("mauvais", hashed))

#bcypt envoie des bytes et pas des strings !! ET hashed contient également le sel le resultat et la formule de calcule
