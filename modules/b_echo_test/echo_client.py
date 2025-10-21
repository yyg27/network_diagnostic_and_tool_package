import socket

def echo_client(message, port = 56458):
    print("\n############ ECHO CLIENT ############");

    host ='localhost';

    client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    server_address = (host,port);

    client_s.connect(server_address);
    print(f"##CLIENT## - Connected to {server_address}");

    client_s.sendall(message.encode());
    print(f"##CLIENT## - Sent: {message}");

    data = client_s.recv(1024);
    print(f"##CLIENT## - Received from server: {data.decode()}");

    client_s.close();
    print("##CLIENT## - Connection closed.\n");


echo_client(message="yyg")

