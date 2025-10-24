import socket
import threading
import logging
import sys

#logging config
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
);

##TCP chat client##
def chat_client(host="localhost", port=56458):
    username = input("Enter your username: ").strip();
    if not username:
        print("Please enter a username!");
        return
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    
    try:
        client.connect((host, port));
    except Exception as e:
        logging.error(f"Connection error: {e}");
        return
    
    logging.info(f"Connected to server at {host},{port}");
    
    def receive_msg():
        while True:
            try:
                message = client.recv(1024).decode('utf-8', errors='ignore');
                if message == "USERNAME":
                    client.send(username.encode('utf-8'));
                elif message:
                    print(message);
                else:
                    raise Exception("Server closed connection");
            except Exception as e:
                print(f"\nDisconnected from server: {e}");
                client.close();
                break
    
    ##function to send messages
    def write():
        while True:
            try:
                message_text = input('')
                if message_text.strip():
                    message = f"{username}: {message_text}"
                    client.send(message.encode('utf-8'));
            except Exception as e:
                print(f"Error sending message: {e}");
                client.close();
                break
    
    ##threading voodoo magic 
    receive_thread = threading.Thread(target=receive_msg, daemon=True);
    receive_thread.start();
    
    write_thread = threading.Thread(target=write, daemon=True);
    write_thread.start();
    
    #keeping the main thread alive
    try:
        receive_thread.join();
    except KeyboardInterrupt:
        print("\nDisconnecting...");
        client.close();

if __name__ == "__main__":
    chat_client();