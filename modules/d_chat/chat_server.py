import socket
import threading
import logging

#logging config
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
);

##TCP chat server##
def chat_server(host="0.0.0.0", port=56458):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
    
    logging.info("### CHAT SERVER ### - Server starting up...");
    
    try:
        server.bind((host, port));
        logging.info(f"### CHAT SERVER ### - Server is bound to port {port}");
        server.listen();
        logging.info(f"### CHAT SERVER ### - Server listening on port {port}..;.");
    except Exception as e:
        logging.error(f"### CHAT SERVER ### - Failed to start server: {e}");
        return
    
    #for storing clients address and usernames
    clients = [];
    usernames = [];
    
    ##function to broadcast messages to all clients
    def broadcast(message):
        for client in clients:
            try:
                if isinstance(message, str):
                    client.send(message.encode("utf-8"));###added isinstance and encoding due to bugs
                else:
                    client.send(message);
            except Exception as e:
                logging.error(f"Error broadcasting to client: {e}");
    
    ##function to handle client messages
    def handle(client):
        while True:
            try:
                message = client.recv(1024).decode("utf-8", errors="ignore");
                if not message:
                    #if client disconnected
                    raise Exception("Client disconnected");
                broadcast(message);
            except:
                #remove client
                if client in clients:
                    index = clients.index(client);
                    clients.remove(client);
                    client.close();
                    username = usernames[index];
                    broadcast(f"### CHAT SERVER ### - {username} has left the chat");
                    usernames.remove(username);
                    logging.info(f"{username} disconnected");
                break
    
    ##function to receive connections
    def receive():
        while True:
            try:
                client, address = server.accept();
                logging.info(f"User connected from {address}");
                
                client.send("USERNAME".encode("utf-8"));
                username = client.recv(1024).decode("utf-8", errors="ignore").strip();
                
                if not username:
                    username = f"User_{address[1]}";
                
                #append to server list
                clients.append(client);
                usernames.append(username);
                
                broadcast(f"### CHAT SERVER ### - {username} has joined the chat");
                client.send("### CHAT SERVER ### - Connected to the server".encode("utf-8"));
                logging.info(f"{username} joined the chat");
                
                #threading
                thread = threading.Thread(target=handle, args=(client,), daemon=True);
                ##daemon=True prevents crashes
                thread.start();
            except Exception as e:
                logging.error(f"Error accepting connection: {e}");
                break
    
    try:
        receive();
    except KeyboardInterrupt:
        logging.info("Server shutting down...");
        for client in clients:
            try:
                client.close();
            except:
                pass
        server.close();

if __name__ == "__main__":
    chat_server();