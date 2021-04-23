from AES_encryption_decryption import rootAES
from RSA_encryption_decryption import rootRSAEncryption
from RSA_signature import  rootRSA
from hashing import  rootHash

conductor =input("Enter 'c' to continue or 'q' to quit: ")
while conductor != 'q':
    print("\t 1. AES Encryption Decryption ")
    print("\t 2. RSA Encryption Decryption ")
    print("\t 3. RSA Signature ")
    print("\t 4. SHA256 Hashing ")
    option = int(input("Select 1 or 2 or 3 or 4: "))

    if option == 1:
        print('---------------Starting AES---------------')
        rootAES()
        print('---------------Ending AES---------------')
    elif option == 2:
        print('---------------Starting RSA Encryption---------------')
        rootRSAEncryption()
        print('---------------Ending RSA Encryption---------------')
    elif option == 3:
        print('---------------Starting RSA Signature---------------')
        rootRSA()
        print('---------------Ending RSA Signature---------------')
    else:
        print('---------------Starting SHA256 Hashing---------------')
        print(rootHash())
        print('---------------Ending SHA256 Hashing---------------')
    conductor = input("Enter 'c' to continue or 'q' to quit : ")
