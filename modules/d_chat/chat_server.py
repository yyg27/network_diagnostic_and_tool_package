import socket
import threading

 ##TCP chat server##
def chat_server(): 
    
    host = "localhost";

    port = 56458;

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print("###CHAT SERVER### - Server starting up...")
    server.bind((host,port));
    print(f"###CHAT SERVER### - Server is bound to{port} port")
    server.listen();
    print(f"###CHAT SERVER### - Server listening on port {port}...")

    #for storing clients address and usernames
    clients = []
    usernames = []

    ##function to broadcast messages to all clients
    def broadcast(message):
           for client in clients:
            client.send(message);

    def handle(client):
            while True:
                try:
                    message = client.recv(1024);
                    broadcast(message);
                except:
                    index = clients.index(client);
                    clients.remove(client); 
                    client.close();
                    username = usernames[index];
                    broadcast(f"{username} has left the chat".encode('utf-8'));   
                    usernames.remove(username);
                    break

##function to recieve
    def recieve():
        while True:
            client,address = server.accept();
            print(f"User connected with {str(address)}");
        
            client.send("USERNAME".encode("utf-8"));
            username = client.recv(1024).decode("utf-8");
        
            ##append to server list
            clients.append(client);
            usernames.append(username);

            broadcast(f"{username} has joined the chat".encode("utf-8"));
            client.send("Connected to the server".encode("utf-8"));

            ##threading
            thread = threading.Thread(target=handle, args=(client,));
            thread.start();

    recieve()
chat_server();
