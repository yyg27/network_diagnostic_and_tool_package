import socket
import logging

#logging config
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
);

def get_machine_info():

    print("#"*54);
    print(" "*20 + " " + "MACHINE INFO" +" " +" "*20);
    print("#"*54+"\n");


    try:
        hostname = socket.gethostname();
        #ip_address = socket.gethostbyname(hostname);
        #socket.gethostbyname(hostname) just returns the loop-back address of 127.0.1.1 for my arch-linux system, not the my real ip address
        #so the solution i found is that you need to create a UDP socket by using SOCK_DGRAM and connect it to the Google's DNS "8.8.8.8" to 
        #trick linux OS to give it's real ip address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
        logging.info(f"Hostname retrieved..");
        s.connect(("8.8.8.8", 80));
        ip_address = s.getsockname()[0];
        logging.info(f"Primary IP retrieved..");
        s.close();
    except Exception as e :
        ip_address = "IP Address not found";
        logging.warning(f"Could not retrieve primary IP {e}");

    ###same problem about linux. Read the bottom for info
    try:
        ip_list = socket.gethostbyname_ex(hostname)[2];
        logging.info(f"All IP's retrieved..");
    except Exception as e:
        ip_list =["IP Address not found"];
        logging.warning(f"Could not retrieve all IP's: {e}");   


    ##display
    print("\n" + "#"*54);
    print("Hostname:",hostname);
    print("Primary IP Address:",ip_address);
    ####BUGGY
    print("Other IP's",ip_list); 
    print("#"*54);

    #ip_list = socket.gethostbyname_ex(hostname)[2] just returns the loop-back address again like the socket.gethostbyname(hostname) for my linux system 
    #i tried to implement the UDP trick that i used for the primary IP but i could't get it to work
    #the solution that i found on the internet is to use a third-party python library called "netifaces" 
    #i don't know if we are allowed to use third-party libraries in our project. So i didn't use it 
    #for this reason this part of my machine_info module is limited for my knowledge and buggy 

    #TO-DO add other version with "netifaces" library

if __name__ == '__main__':
    get_machine_info();