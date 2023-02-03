import socket
import threading
##import rsa
import hashlib

from cryptography.fernet import Fernet

## public_key,private_key= rsa.newkeys(1024)
## public_key=None
# key = Fernet.generate_key()
# fer=Fernet(key)
# encMessage = fernet.encrypt(message.encode())
# decMessage = fernet.decrypt(encMessage).decode()


choose=input("Do you want to host(1) or connect(2)?")
if choose=="1":
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))
    server.listen()

    client, _ = server.accept()
    passwd = input("Enter password for encrypted chat : ") 
    klg=(decrypt(passwd,client.recv(1024)).decode('utf-8'))
    ## client.send(public_key.save_pkcs1("FORMAT = PEM"))
    ## public_partner= rsa.PublicKey.load_pkcs1(client.recv(1024))
elif choose=="2":
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("0.0.0.0" , 8080))
    klg=(decrypt(passwd,client.recv(1024)).decode('utf-8'))
    passwd = input("Enter password for encrypted chat : ") 
    ##public_partner= rsa.PublicKey.load_pkcs1(client.recv(1024))
    ##client.send(public_key.save_pkcs1("FORMAT = PEM"))
else:
    exit()

def sendingmessages(c):
    #passwd = input("Enter password for encrypted chat : ") 
    
    while True:
        #print(decrypt(passwd,client.recv(1024)).decode('utf-8'))
        message=input("Enter your text here:")
        encMessage = hashlib.sha512(message.encode())
        ###encMsg = encrypt(passwd,("You:"+ message))
        client.send(encMessage)
        print("You:"+ message)

        # result_sender=hashlib.sha512(message.encode())
        # #key = Fernet.generate_key()
        # result_sender.hexdigest()
        # #fer=Fernet(key)
        #encMessage = hashlib.sha512(message.encode())
        #decMessage = hashlib.sha512(encMessage.decode())
        #c.send(message.encode())
        #print("You:"+ message)

def recievemessages(c):
        while True:
            # key = Fernet.generate_key()
            # fer=Fernet(key)
            # encMessage = fernet.encrypt(message.encode())
            # decMessage = fernet.decrypt(encMessage).decode()
            print("Them:"+ hexdigest(client.recv(1024),passwd).decode())

threading.Thread(target=sendingmessages, args=(client,)).start()
threading.Thread(target=recievemessages, args=(client,)).start()

        
# ip="127.0.0.1"
# port=1234

# 
# server.bind((ip, port))
# 
# while True:
#     client,address= server.accept()
#     print(f"Connection established -{address[0]} : {address [1]}")