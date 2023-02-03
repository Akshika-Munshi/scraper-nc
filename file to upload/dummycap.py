import socket
import threading
import hmac
import hashlib
import string
import base64

choose=input("Do you want to host(1) or connect(2)?")
if choose=="1":
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("10.113.22.196", 8080))
    print("Connection done")
    server.listen()
    
    client, _ = server.accept()

elif choose=="2":
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("10.113.22.196",8080))
else:
    exit()

def sendingmessages(c):
    while True:
        message=input("")
        c.send(message.encode())
        print("You:"+ message)
    
def recievemessages(c):
        while True:
            print("Them:"+ c.recv(1024).decode())

threading.Thread(target=sendingmessages, args=(client,)).start()
threading.Thread(target=recievemessages, args=(client,)).start()
