# learning resource : https://www.codegrepper.com/code-examples/python/rsa+encryption+python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time as clock
from drawGraph import plotGraph


def generateKey(key):
    keyPair = RSA.generate(key)
    pubKey = keyPair.publickey()
    publicKeyPEM = pubKey.exportKey()
    privateKeyPEM = keyPair.exportKey()
    file = open('RSA_keys.txt', 'r+')
    file.write(str(publicKeyPEM))
    file.write(str(privateKeyPEM))
    return keyPair, pubKey


def performEncrypt(filename, pubKey):
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
    data = dict()
    for i in range(1, 5):
        start = clock.time()
        keypair, pubKey = generateKey(1024*i)
        encrypted_texts = performEncrypt('RSA_plain_text.txt', pubKey)
        performDecrypt(keypair,encrypted_texts)
        end = clock.time()
        key = str(1024*i) + '_bits'
        data[key] = end - start
    return data

data =rootRSAEncryption()
plotGraph(data,"RSA Decryption Time")