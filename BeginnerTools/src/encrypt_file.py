from cryptography.fernet import Fernet

class Encryption(object):
    def __init__(self) -> None:
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
        
    def encrypt(self, data):
        return self.cipher_suite.encrypt(data.encode())
    
    def decrypt(self, data):
        return self.cipher_suite.decrypt(data).decode()
    
    def save_key(self, path):
        with open(path, 'wb') as file:
            file.write(self.key)
        
    def load_key(self, path):
        with open(path, 'rb') as file:
            self.key = file.read()
            self.cipher_suite = Fernet(self.key)
            
    def encrypt_file(self, file_path, output_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        encrypted_data = self.cipher_suite.encrypt(data)
        with open(output_path, 'wb') as file:
            file.write(encrypted_data)
            
    def decrypt_file(self, file_path, output_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        decrypted_data = self.cipher_suite.decrypt(data)
        with open(output_path, 'wb') as file:
            file.write(decrypted_data)
            
    def encrypt_text(self, text):
        return self.cipher_suite.encrypt(text.encode())
    
    def decrypt_text(self, text):
        return self.cipher_suite.decrypt(text).decode()
    
