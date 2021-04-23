# https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
from secrets import token_bytes
from Crypto.Cipher import AES
from Crypto import Random


class AES_Encryption:
    def __init__(self, number_of_byte, mode):
        self.mode = mode
        self.iv = Random.new().read(AES.block_size)
        self.key = token_bytes(number_of_byte)
        file = open('AES_keys.txt', 'r+')
        file.write(str(self.key))
        if self.mode == AES.MODE_ECB:
            self.cipher = AES.new(self.key, self.mode)
        else:
            self.cipher = AES.new(self.key, self.mode, self.iv)
        file = open('AES_plain_text.txt', 'r')
        self.plain_text = file.read()
        self.encrypted_text = ''
        self.padded_text = ''

    def pad_message(self, message):
        while len(message) % 16 != 0:
            message = message + ' '
        return message

    def encrypt(self):
        if self.mode == AES.MODE_ECB:
            self.padded_text = self.plain_text if len(self.plain_text) % 16 == 0 else self.pad_message(self.plain_text)
        else:
            self.padded_text = self.plain_text
        self.encrypted_text = self.cipher.encrypt(bytes(self.padded_text.encode()))
        file = open('AES_encrypted_text.txt', 'r+')
        file.write(str(self.encrypted_text))

    def decrypt(self):
        if self.mode == AES.MODE_CFB:
            another_cipher = AES.new(self.key, self.mode, self.iv)
            return another_cipher.decrypt(self.encrypted_text)
        return self.cipher.decrypt(self.encrypted_text)


def rootAES():
    mode_option = int(input("select 1 for ECB mode 2 for CFB mode : "))
    mode = AES.MODE_ECB if mode_option == 1 else AES.MODE_CFB
    number_of_byte = int(input("number of bytes of key length: "))

    encryption = AES_Encryption(number_of_byte, mode)
    encryption.encrypt()
    decrypted_text = encryption.decrypt().strip()
    print(f'Decrypted text: {decrypted_text}')


