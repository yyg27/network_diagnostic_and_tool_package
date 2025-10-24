import socket
import logging
import sys

#log config
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
    );

def change_settings(
    host='8.8.8.8', ##target host
    port=53, ##target port
    timeout=5, ##socket timeout
    send_buf_size=4096, ##send buffer size
    recv_buf_size=4096,  ##recieve buffer size
    blocking=True ##use blocking or non-blocking mode true -> blocking
    ):

    print("#"*71);
    print(" "*20 + " " + "ERROR MANAGEMENT AND SETTINGS" +" " +" "*20);
    print("#"*71+"\n");
    

    s = None

    try:
        #creating a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        logging.info("Socket has been created successfully");

        #configure socket timeout
        s.settimeout(timeout);
        logging.info(f"##Settings## - Socket timeout set to {timeout} seconds");

        #configure send and receive buffer sizes
        s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, send_buf_size);
        s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, recv_buf_size);
        logging.info(f"##Settings## - Send buffer is set to {s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)} bytes");
        logging.info(f"##Settings## - Receive buffer set to {s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)} bytes");

        #configure blocking and non-blocking mode
        if blocking == False:
            s.setblocking(False);
            logging.info(f"##Settings## - Socket switched to NON-blocking mode .");
            ##gives socket error
        else:
            s.setblocking(True)
            logging.info(f"##Settings## - Socket switched to blocking mode .");
        
        logging.info(f"Attempting connection to {host},{port}...");
        s.connect((host, port));
        logging.info(f"SUCCESS: Connected to {host},{port}");

    except socket.timeout:
        logging.error(f"ERROR: Connection to ({host}:{port}) timed out after {timeout} seconds");
        
    except ConnectionRefusedError:
        logging.error(f"ERROR: Connection refused by {host},{port}");

    except socket.error as e:
        logging.error(f"ERROR: Socket error - {e}");
    
    except Exception as e:
        #unexpected error
        logging.error(f"✗ ERROR: Unexpected error - {type(e).__name__}: {e}");

    finally:
        #close the socket
        if s:
            s.close();
            logging.info("Socket closed");

change_settings();


