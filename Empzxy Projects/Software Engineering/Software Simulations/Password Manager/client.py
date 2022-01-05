import socket 
import os 
import sys 
import pickle 
import pandas 

IP = "localhost"
PORT = 7302 


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

class Client():
    passwords = {}
    empty = {}

    def start():
        print(
            '--------------------------------------- \n----------------Menu------------------- \n1. Create new Password \n2. Find all Saved Passwords \n3. Delete Previous Password \nQ. Exit\n---------------------------------------'
        )
        choice = input(": ")
       
        if choice == "2":
            Client.search_for_password()
        elif choice == "1":
            Client.create_password()
        elif choice == "q" or choice == "Q":
            f = open("password_data.pkl", "rb")
            l = os.path.getsize("password_data.pkl")
            m = f.read(l)
            client_socket.send(m)
            f.close()
            f = open("password_data.pkl", "wb")
            f.write(Client.empty, f)
            f.close()
            sys.exit()
        elif choice == "3":
            print('This Feature isnt avaiable At the moment.')
        else:
            Client.start()
        
    def search_for_password():
        data = pandas.read_pickle("password_data.pkl")
        
        print('\n---------------------------------------\n--------------Results------------------\n |')
        print(data)
        
        Client.start()

    def create_password():
        print('--------------------------------------- \nPlease provide the email linked to the password.')
        username_of_password = input(": ")
        print('--------------------------------------- \nPlease Enter the url (site) for the password.')
        name_of_password = input(": ")
        print('--------------------------------------- \nPlease type in the Password. ')
        password_of_password = input(": ")
        print('---------------------------------------')

        full_password = "Url: " + name_of_password + "\n Email: " + username_of_password + "\n Password: " + password_of_password + "\n---------------------------------------"

        print('--------------Results------------------\n', full_password)

        isOk = input("Is this your password? (Y or N) ")

        if isOk == "Y" or isOk == "y":
            Client.passwords[name_of_password] = "Username: " + username_of_password + "Password: " + password_of_password
            with open('password_data.pkl', 'wb') as pickle_file:
                pickle.dump(Client.passwords, pickle_file)

            Client.start()

        elif isOk == "N" or isOk == "n":
            Client.create_password()
        else:
            print("Taking back to start. (Unidentified Character)")
            Client.start()

while True:
    empty_list = {}

    password_data = open("password_data.pkl", "wb")
    pickle.dump(empty_list, password_data)

    print("Attempting to accept passwords, please accept delay...")
    serverPasswords = client_socket.recv(8194)
    password_data = open("password_data.pkl", "wb")
    pickle.dump(serverPasswords, password_data)
    password_data.close()
    print("Done! - Merry Christmas!")
    Client.start()
