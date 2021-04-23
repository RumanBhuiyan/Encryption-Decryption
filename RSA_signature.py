# learning resource : https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii

keyPair = RSA.generate(bits=1024)
pubKey = keyPair.publickey()


def generateSignature(filename):
    file = open(filename, 'r')
    filedata = file.read()
    hash = SHA256.new(bytes(filedata.encode()))
    scheme = PKCS115_SigScheme(keyPair)
    signature = scheme.sign(hash)
    file = open('RSA_signature.txt', 'r+')
    file.write(str(signature))
    print("Signature:", binascii.hexlify(signature))
    return signature


def verifySignature(filename, signature):
    file = open(filename, 'r')
    filedata = file.read()
    hash = SHA256.new(bytes(filedata.encode()))
    verifier = PKCS115_SigScheme(pubKey)
    try:
        verifier.verify(hash, signature)
        print("Signature is valid.")
    except:
        print("Signature is invalid.")


def rootRSA():
    file_signature = generateSignature('RSA_plain_text.txt')
    verifySignature('RSA_plain_text.txt', file_signature)

