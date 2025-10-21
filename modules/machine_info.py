import socket

def get_machine_info():
    hostname = socket.gethostname();
    #ip_address = socket.gethostbyname(hostname);
    #socket.gethostbyname(hostname) just returns the loop-back address of 127.0.1.1 for my arch-linux system, not the my real ip address
    #so the solution i found is that you need to create a UDP socket by using SOCK_DGRAM and connect it to the Google's DNS "8.8.8.8" to 
    #trick linux OS to give it's real ip address
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
        s.connect(("8.8.8.8", 80));
        ip_address = s.getsockname()[0];
        s.close();        

    except:
        ip_address = "IP Address not found"

    ### same problem about linux. Read the bottom for info
    try:
        ip_list = socket.gethostbyname_ex(hostname)[2]
    except:
        ip_list =["Ip Address not found"]        


    print("Hostname:",hostname);
    print("Primary IP Address:",ip_address);
    ####
    print("Other IP's",ip_list) 

    #ip_list = socket.gethostbyname_ex(hostname)[2] just returns the loop-back address again like the socket.gethostbyname(hostname) for my linux system 
    #i tried to implement the UDP trick that i used for the primary IP but i could't get it to work
    #the solution that i found on the internet is to use a third-party python library called "netifaces" 
    #i don't know if we are allowed to use third-party libraries in our project. So i didn't use it 
    #for this reason this part of my machine_info module is buggy 

get_machine_info();