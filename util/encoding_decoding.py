#importamo fernte que nos ayudara mucho
from cryptography.fernet import Fernet

#creamos 2 metodos 
#encriptamos
def encrypted(password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g=')
    b_password = bytes(password, 'ascii')
    encrypted_password = f.encrypt(b_password)
    return encrypted_password.decode('ascii')
#desencriptamos
def decrypt(password:str):
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g=')
    b_password = bytes(password, 'ascii')
    b_password_decrypt = f.encrypt(b_password)
    return b_password_decrypt.decode('ascii')

