import rsa
import json
import base64

class AITrackerOracle:
    def __init__(self,public_key_ml_filepath,private_key_oracle_filepath):
        self.publicKeyML = self.__import_public_key(public_key_ml_filepath)
        self.privateKeyOracle = self.__import_private_key(private_key_oracle_filepath)

    def __import_public_key(self,filepath):
        f_pub_read = open(filepath,'rb')
        publicKeyFromFIle = f_pub_read.read()
        publicKey = rsa.PublicKey.load_pkcs1(publicKeyFromFIle)
        f_pub_read.close()
        return publicKey
    
    def __import_private_key(self,filepath):
        f_read = open(filepath,'rb')
        privateKeyFromFIle = f_read.read()
        privateKey = rsa.PrivateKey.load_pkcs1(privateKeyFromFIle)
        f_read.close()
        return privateKey

    def decrypt(self,encrypted):
        encrypted_bytes = base64.b64decode(encrypted)
        decrypted = rsa.decrypt(encrypted_bytes, self.privateKeyOracle)
        decrypted = decrypted.decode('utf8')
        return decrypted

    def verify(self,message,signature):
        signature = base64.b64decode(signature)
        message = message.encode()
        try:
            rsa.verify(message, signature, self.publicKeyML)
        except:
            return False
        return True