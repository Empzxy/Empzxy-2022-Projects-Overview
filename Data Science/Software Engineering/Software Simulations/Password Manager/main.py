import socket
import os 
import pickle

IP = "localhost"
PORT = 7302 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen(1)

Check_for_Client = True
Check_for_Data = False

while Check_for_Client:
    print("Waiting for User...")
    client_socket, client_address= server_socket.accept()

    print("User has joined at ip: "+ str(client_address) + "!")

    f = open("data.pkl", "rb")
    l = os.path.getsize("data.pkl")
    m = f.read(l)
    client_socket.send(m)
    print("Done sending...")
    Check_for_Data = True
    while Check_for_Data:
        print("Waiting For User To Finish...")

        try:
            data = client_socket.recv(8194)
            if data:
                f = open("data.pkl", "wb")
                f.write(data)
                f.close()
                Check_for_Data = False
        except:
            Check_for_Data = True 
