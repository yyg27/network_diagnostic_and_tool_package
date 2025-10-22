import socket
import threading

 ##TCP chat server##
def chat_server(): 
    
    host = "localhost";

    port = 55458;

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
                broadcast(f"{username} has left the chat".encode('ascii'));   
                usernames.remove(username);
                break

##function to reciv
def recive():
    while True:
        client,address = server.accept();
        print(f"User connected with {str(address)}");
        
        client.send("USER".encode("ascii"));
        username = client.recv(1024).decode("ascii");
        
        ##append to server list
        clients.append(client);
        usernames.append(username);

        broadcast(f"{username} has joined the chat".encode("ascii"));
        client.send("Connected to the server".encode("ascii"));

        ##threading
        thread = threading.Thread(target=handle, args=(client,));
        thread.start();

    recive();
chat_server();
