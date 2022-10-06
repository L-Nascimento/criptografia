import random  # Será usada para gerar uma senha aleatória
import string


class DILET:
    def __init__(self):  # Inicializa classe
        self.const_caracters = (
            " ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+",
            ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7",
            "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C",
            "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[",
            "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g",
            "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
            "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~")
        self.new_caracter_sequence = []

    def _fill_new_caracters(self):
        for letter in self.const_caracters:
            if not self.new_caracter_sequence.__contains__(letter):
                self.new_caracter_sequence.append(letter)

    def create_password(self):  # Cria a senha para a criptografia
        password = ""
        for i in range(0, 52):
            password += random.choice(string.ascii_letters)
        return password

    def encrypt(self, plain_text, password):  # Encripita texto enviado
        encrypt_text = ""
        self.new_caracter_sequence.clear()
        for letter in password:
            self.new_caracter_sequence.append(self.const_caracters[self.const_caracters.index(letter)])
        self._fill_new_caracters()
        for letter in plain_text:
            encrypt_text += self.new_caracter_sequence[self.const_caracters.index(letter)]
        return encrypt_text

    def decrypt(self, encrypt_text, password):
        decrypt_text = ""
        self.new_caracter_sequence.clear()
        for letter in password:
            self.new_caracter_sequence.append(self.const_caracters[self.const_caracters.index(letter)])
        self._fill_new_caracters()
        for letter in encrypt_text:
            decrypt_text += self.const_caracters[self.new_caracter_sequence.index(letter)]
        return decrypt_text
