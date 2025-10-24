import socket
import logging
import sys

#logging config
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
);

def echo_client(message, port = 56458):
    
    print("#"*53);
    print(" "*20 + " " + "ECHO CLIENT" +" " +" "*20);
    print("#"*53+"\n");

    host ='localhost';

    try:
        client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

        server_address = (host,port);

        logging.info(f"## CLIENT ## - Connecting to {server_address}");
        client_s.connect(server_address);
        logging.info(f"## CLIENT ## - Connected to {server_address}");

        client_s.sendall(message.encode());
        logging.info(f"## CLIENT ## - Sent: {message}");

        data = client_s.recv(1024);
        recieved_message = data.decode();
        logging.info(f"## CLIENT ## - Received from server: {recieved_message}");

        if recieved_message == message:
            logging.info("### Echo Test SUCCESSFUL ###");
        else:
            logging.warning("### Error... Echo Test FAILED ###");

    except ConnectionRefusedError:
        logging.error(f"Connection refused by {host}:{port}")
    except socket.error as e:
        logging.error(f"Socket error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally: 
        logging.info("## CLIENT ## - Closing connection...");
        client_s.close();
        logging.info("## CLIENT ## - Connection closed.\n");


if __name__ == "__main__":
    #get message from client or use default
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
    else:
        message = input("Enter message to test echo: ") or "MARCO" #don't say POLO

    echo_client(message);