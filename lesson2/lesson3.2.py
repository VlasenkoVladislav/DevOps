import pyAesCrypt

password = "123"
#encrypt_file
def encrypt_file(input_file):
    output_file = input_file + ".aes"
    pyAesCrypt.encryptFile(input_file, output_file, password)
    folder_str = ".\\DevOps\\"
encrypt_file("D:\\DevOps\\123.txt")

#decrypt_file
def decrypt_file(input_file):
    output_file = input_file.replace(".aes", "") 
    pyAesCrypt.decryptFile(input_file, output_file, password)
decrypt_file("D:\\DevOps\\123.txt.aes")