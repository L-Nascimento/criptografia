from DILET import DILET

print("=-" * 20)
cripto = DILET()
password = cripto.create_password()
plain_text = input("Digite a frase para encriptar: \n")
encrypt_text = cripto.encrypt(plain_text, password)
decrypt_text = cripto.decrypt(encrypt_text, password)
print(f"Mensagem original: {plain_text}"
      f"\nSenha de criptografia: {password}"
      f"\nEncriptada: {encrypt_text}"
      f"\nDecriptada: {decrypt_text}")
