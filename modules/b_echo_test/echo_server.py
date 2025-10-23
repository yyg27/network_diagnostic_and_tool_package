import socket
import logging

#logging config
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
);

def echo_server(port = 56458):
    
    print("#"*53);
    print(" "*20 + " " + "ECHO SERVER" +" " +" "*20);
    print("#"*53+"\n");

    host ='localhost';
    try:
        #Creating a TCP socket 
        server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        logging.info("## SERVER ## - Socket has been created");
        #Reuse address/port fix
        server_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
        server_address = host,port;
        #server_s.bind(("0.0.0.0",port));
        server_s.bind(server_address);
        logging.info(f"## SERVER ## - Server is bound to {server_address}");

        server_s.listen(5);
        logging.info(f"## SERVER ## - Listening on port {port}...");
        logging.info("Waiting for connections... (Press Ctrl+C to stop)");
    
        while True:
            try:
                connection, client_address = server_s.accept();
                logging.info(f"## SERVER ## - Connected by {client_address}");

                data = connection.recv(1024)
                if not data:
                    logging.warning("## SERVER ## - No data received, closing connection.");
                    connection.close();
                    continue

                logging.info(f"## SERVER ## - Received: {data.decode()}");
        
                #ECHO
                connection.sendall(data);
                logging.info("## SERVER ## - Echoed data back to client.");

            except Exception as e:
                logging.error(f"Error handling client: {e}")
            finally:
                connection.close();
                logging.info("## SERVER ## - Connection closed.\n");

    except KeyboardInterrupt:
        logging.info("\n## SERVER ## - Server stopped by user");
    except Exception as e:
        logging.info(f"## SERVER ## - Error: {e}");
    finally:
        server_s.close();
        logging.info("## SERVER ## - Server socket closed");

if __name__ == "__main__":
    echo_server(56458)

