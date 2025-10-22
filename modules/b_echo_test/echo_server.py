import socket

def echo_server(port = 56458):
    print("\n############ ECHO SERVER ############");

    host ='localhost';
    
    #Creating a TCP socket 
    server_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    print("\n##SERVER## - Socket has been created");
    #Reuse address/port fix
    server_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = (host,port);
    #server_s.bind(("0.0.0.0",port));
    server_s.bind(server_address);
    print(f"##SERVER## - Server is bound to {server_address}");

    server_s.listen(5);
    print(f"##SERVER## - Listening on port {port}...");

    try:
        while True:

            connection, client_address = server_s.accept();
            print(f"##SERVER## - Connected by {client_address}");

            data = connection.recv(1024)
            if not data:
                print("##SERVER## - No data received, closing connection.");
                connection.close();
                continue

            print(f"##SERVER## - Received: {data.decode()}");
        
            #ECHO
            connection.sendall(data);
            print("##SERVER## - Echoed data back to client.");

            connection.close();
            print("##SERVER## - Connection closed.\n");

    except KeyboardInterrupt:
        print("\n##SERVER## - Server stopped by user");
    except Exception as e:
        print(f"##SERVER## - Error: {e}")
    finally:
        server_s.close()
        print("##SERVER## - Server socket closed")       

echo_server(56458)

