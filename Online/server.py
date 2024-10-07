import socket, json, pickle, threading, multiprocessing
from functions import main

host = "127.0.0.1"
port = 23333
s = []

class Server():
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host,port))
        self.sock.listen(5)
        self.sock.settimeout(0.5)
        try:
            while True:
                try:
                    conn, addr = self.sock.accept()
                    m = multiprocessing.Process(target=handler,args=(conn,addr))
                    m.daemon=True
                    m.start() 
                except socket.timeout:
                    # print("Timeout")
                    pass
                except KeyboardInterrupt:
                    pass
        except KeyboardInterrupt:
            print("Server closed with KeyboardInterrupt!")
            self.sock.close()
        

def handler(conn, addr):
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                print("x Client disconnected!")
                break
            else:
                print("> Message from client: {}".format(json.loads(data)))
                msg = json.loads(data)
                print(msg)
                if msg[0] == "login": ## LOGIN
                    response = main.login(msg[1]) ## -1 if not login. Otherwise, return id user
                    print(response)
                    conn.sendall(str(response).encode())
                elif msg[0] == "summon": ## SUMMON
                    #print("summon")
                    #s.append(str(conn.fileno()))
                    response = main.invocar(int(msg[1]))
                    print(response)
                    conn.sendall(pickle.dumps(response))
                elif msg[0] == "play": ## PLAY MATCH
                    response = "play"
                #msg = "> Message from server".format(data.decode()).encode()
                
    except:
        pass
    finally:
        conn.close()
        

if __name__ == "__main__":
    server = Server(host, port)
    try:
        server.start()
    except:
        pass
    finally:
        for process in multiprocessing.active_children():
            process.terminate()
            process.join()