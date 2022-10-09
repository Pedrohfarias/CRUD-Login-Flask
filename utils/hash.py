import bcrypt


#Gerador de hash
def generate_hash(pwd):
    try:
        byte_pwd = pwd.encode('utf-8')
        my_salt = bcrypt.gensalt()
        return bcrypt.hashpw(byte_pwd, my_salt)
    except:
        print("Error generating hash")
        return None
        

#Verifica se o hash ta correto
def check_hash(pwd, hash):
    try:
        byte_pwd = pwd.encode('utf-8')
        byte_hash = hash.encode('utf-8')
        return bcrypt.checkpw(byte_pwd, byte_hash)
    except:
        print("Error checking hash")
        return False
        



