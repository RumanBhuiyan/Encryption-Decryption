# learning resource : https://www.codegrepper.com/code-examples/python/rsa+encryption+python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


def generateKey():
    keyPair = RSA.generate(3072)
    pubKey = keyPair.publickey()
    publicKeyPEM = pubKey.exportKey()
    privateKeyPEM = keyPair.exportKey()
    file = open('RSA_keys.txt', 'r+')
    file.write(str(publicKeyPEM))
    file.write(str(privateKeyPEM))
    return keyPair,pubKey


def performEncrypt(filename,pubKey):
    file = open(filename, 'r')
    filedata = file.read()
    plain_texts = bytes(filedata, 'utf-8')
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted_texts = encryptor.encrypt(plain_texts)
    print("Encrypted:", binascii.hexlify(encrypted_texts))
    file = open('RSA_encrypted.txt', 'r+')
    file.write(str(encrypted_texts))
    return encrypted_texts


def performDecrypt(keypair, encrypted_texts):
    decryptor = PKCS1_OAEP.new(keypair)
    decrypted = decryptor.decrypt(encrypted_texts)
    print('Decrypted:', decrypted.decode('utf-8'))

def rootRSAEncryption():
    keypair, pubKey = generateKey()
    encrypted_texts =performEncrypt('RSA_plain_text.txt', pubKey)
    performDecrypt(keypair, encrypted_texts)



