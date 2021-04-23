# Learning resource : https://www.quickprogrammingtips.com/python/how-to-calculate-sha256-hash-of-a-file-in-python.html
import hashlib


def getHashOfFile(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()


def rootHash():
    return getHashOfFile('hashing_plain_text.txt')


