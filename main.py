from cryptography.fernet import Fernet


print("digite a frase para encriptar")
original = input()

key = Fernet.generate_key()
fernet = Fernet(key)

enc = fernet.encrypt(original.encode())

desc = fernet.decrypt(enc).decode()

print("Mensagem original: ", original)
print("Encriptada: ", enc)
print("Descriptada: ", desc)







