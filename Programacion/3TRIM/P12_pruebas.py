import hashlib

def hashearContrasenia(hash_password):
    hash_obj = hashlib.sha256()
    hash_obj.update(hash_password.encode('utf-8'))
    contraseniaCifrada = hash_obj.hexdigest()
    return contraseniaCifrada

contrasenia = input("cont: ")
contraseniahash = hashearContrasenia(contrasenia)
print(len(contraseniahash))