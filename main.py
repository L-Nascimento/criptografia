from cryptography.fernet import Fernet
from DILET import DILET

print("digite a frase para encriptar")
original = input()
key = Fernet.generate_key()  # todo: substituir por create_password do DILET
fernet = Fernet(key)  # todo: no caso do DILET essa linha não será necessária
enc = fernet.encrypt(original.encode())  # todo: substituir por encrypt do DILET
desc = fernet.decrypt(enc).decode()  # todo: substituir pelo decrypy do DILET
print("Mensagem original: ", original)
print("Encriptada: ", enc)
print("Descriptada: ", desc)
