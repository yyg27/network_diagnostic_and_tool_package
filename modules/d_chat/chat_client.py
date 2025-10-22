import socket
import threading

## TCP chat client##
def chat_client():
    username = input("Enter your username: ");

    host = "localhost";
    port = 56458
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    client.connect((host, port));

    def receive_msg():
        while True:
            try:
                message = client.recv(1024).decode('utf-8');
                if message == "USERNAME":
                    client.send(username.encode('utf-8'));
                else:
                    print(message);
            except:
                print("An error occurred! Disconnecting...");
                client.close();
                break

    ##function to send messages
    def write():
        while True:
            message = f"{username}: {input('')}";
            client.send(message.encode('utf-8'));

    ##threading vodoo magic 
    receive_thread = threading.Thread(target=receive_msg);
    receive_thread.start();

    write_thread = threading.Thread(target=write);
    write_thread.start();

chat_client();
