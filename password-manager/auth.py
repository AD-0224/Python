import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password) 
#bcrypt uses bytes instead of strings.

def save_master_password(password):
    hashed = hash_password(password)
    with open("master.hash", "wb") as file:
        file.write(hashed)

def check_master_password(password):
      with open("master.hash", "rb") as file:
        hashed = file.read()
        
      return verify_password(password, hashed)
