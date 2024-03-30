import base64

def encrypt(pas):
    encode = base64.b64encode(pas.encode())
    print(f"The Encode value : {encode}")

def decrypt(de):
    decode =base64.b64decode(de)
    decode_d=decode.decode()
    print(f"The Decoded value : {decode_d}")

print("1:Encrypt 2:Decrypt\n")
print("Only base64 encrypted text will be decrypt")

n=int(input("Enter a number :"))

if (n==1):
    password = input("Enter your Text :")
    encrypt(password)
elif (n==2):
    de = input("Enter a encrypt text here to decrypt :")
    decrypt(de)
else:
    print("Invalid Number")

