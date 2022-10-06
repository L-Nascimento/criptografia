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
            "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "~",
            "~", "~"
        )
        self.new_caracter_sequence = []

    def __fill_new_caracters(self):
        for letter in self.const_caracters:
            if not self.new_caracter_sequence.__contains__(letter):
                self.new_caracter_sequence.append(letter)

    def _fill_new_caracters_with_password(self, password):
        for letter_pos in range(0, 52, 2):
            letter_1 = str(ord(password[letter_pos]))[-1]
            letter_2 = str(oct(ord(password[letter_pos + 1])))[-1]
            self.new_caracter_sequence.append(self.const_caracters[int(letter_1 + letter_2)])
        self.__fill_new_caracters()

    def create_password(self):  # Cria a senha para a criptografia
        password = ""
        for i in range(0, 52):
            password += random.choice(string.ascii_letters)
        return password

    def encrypt(self, plain_text, password):  # Encripita texto enviado
        encrypt_text = ""
        self.new_caracter_sequence.clear()
        self._fill_new_caracters_with_password(password)
        for letter in plain_text:
            encrypt_text += self.new_caracter_sequence[self.const_caracters.index(letter)]

        print(self.new_caracter_sequence)
        print(self.new_caracter_sequence.index(plain_text[0]))
        print(self.new_caracter_sequence.index(plain_text[1]))
        print(len(self.new_caracter_sequence))

        print(self.const_caracters)
        print(self.const_caracters[self.new_caracter_sequence.index(plain_text[0])])
        print(self.const_caracters[self.new_caracter_sequence.index(plain_text[1])])
        print(len(self.const_caracters))

        return encrypt_text

    def decrypt(self, encrypt_text, password):
        decrypt_text = ""
        self.new_caracter_sequence.clear()
        self._fill_new_caracters_with_password(password)
        for letter in encrypt_text:
            decrypt_text += self.const_caracters[self.new_caracter_sequence.index(letter)]
        return decrypt_text
