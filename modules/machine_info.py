import socket;

def get_machine_info():
    hostname = socket.gethostname();
    #ip_address = socket.gethostbyname(hostname);
    #socket.gethostbyname() just returns the loop-back address of 127.0.1.1 for my arch-linux system
    #not the real ip address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
    s.connect(("8.8.8.8", 80));
    ip_address = s.getsockname()[0];
    s.close();


    print("Hostname:",hostname);
    print("IP Address:",ip_address);

get_machine_info();
