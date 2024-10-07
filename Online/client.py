import socket
import json, pickle

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 23333  # The port used by the server

def login(socket: socket):
    print("Inserte usuario: ")
    user = input()
    socket.sendall(json.dumps(("login",user)).encode())
    login_success = socket.recv(1024).decode()
    while login_success == "-1":
        print("Usuario incorrecto\n")
        print("Inserte usuario: ")
        user = input()
        socket.sendall(json.dumps((1,user)).encode())
        login_success = socket.recv(1024).decode()
    return login_success

def summon(socket: socket, id_user: str):
    socket.sendall(json.dumps(("summon",id_user)).encode())
    response = pickle.loads(socket.recv(4096))
    print(response)
    


def main():
    print("Bienvenido a AutoChessPoke\n".center(70))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        id_user = login(s)
        while True:
            msg = input("Introduzca acción: \n1: Invocar 2: Jugar")
            if msg == "1":
                summon(s,id_user)
            else:
                msg = "play"
            #if msg == "Salir":
            break
            
        
        
if __name__ == "__main__":
    main()