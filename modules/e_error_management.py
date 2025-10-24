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
    
    ##added for printing results
    result = {
        'success': False,
        'error_type': None,
        'error_message': None,
        'settings_applied': {}
    }

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
        result['success'] = True

    except socket.timeout:
        result['error_type'] = 'timeout'
        result['error_message'] = f"Connection timeout after {timeout} seconds"
        logging.error(f"ERROR: Connection to ({host}:{port}) timed out after {timeout} seconds");
        
    except ConnectionRefusedError:
        result['error_type'] = 'connection_refused';
        result['error_message'] = f"Connection refused by {host},{port}";
        logging.error(f"ERROR: Connection refused by {host},{port}");
        logging.error("No service listening on port");

    except socket.error as e:
        result['error_type'] = 'socket_error'
        result['error_message'] = str(e);
        logging.error(f"ERROR: Socket error - {e}");

    except socket.gaierror as e:
        #DNS/hostname resolution error
        result['error_type'] = 'dns_error'
        result['error_message'] = f"Cannot resolve hostname: {host}"
        logging.error(f"ERROR: {result['error_message']} - {e}")
        
    except OSError as e:
        #network unreachable error
        result['error_type'] = 'os_error'
        result['error_message'] = str(e)
        logging.error(f"ERROR: OS Error - {e}")

    except BlockingIOError:
        #non-blocking connection in progress
        result['error_type'] = 'non_blocking_in_progress'
        result['error_message'] = 'Connection in progress (non-blocking mode)'
        logging.warning(f"Non-blocking: connection in progress to {host},{port}");
    
    except Exception as e:
        #unexpected error
        result['error_type'] = 'unexpected_error'
        result['error_message'] = f"{type(e).__name__}: {e}"
        logging.error(f"✗ ERROR: Unexpected error - {type(e).__name__}: {e}");

    finally:
        #close the socket
        if s:
            s.close();
            logging.info("Socket closed");

    return result;        

#change_settings(); 


def error_tests():
    print("#"*64);
    print(" "*20 + " " + "ERROR MANAGEMENT TESTS" +" " +" "*20);
    print("#"*64+"\n");

    test_scenarios = [
        {
            'name': 'Test 1: Connection Refused Error', ##no listening server on localhost
            'host': '127.0.0.1',
            'port': 65432,
            'timeout': 3,
            'blocking': True
        },
        {
            'name': 'Test 2: Timeout Error',
            'host': '8.8.8.8', ##google dns only listens to 53 port
            'port': 81,
            'timeout': 1,
            'blocking': True
        },
        {
            'name': 'Test 3: Successful Connection',
            'host': '8.8.8.8',
            'port': 53,
            'timeout': 3,
            'blocking': True
        },
        {
            'name': 'Test 4: Non-Blocking Mode Failure', ##connectionRefusedError because of blocking
            'host': '8.8.8.8',
            'port': 53,
            'timeout': 3,
            'blocking': False
        },
        {
            'name': 'Test 5: DNS Resolution Error',
            'host': 'yigitgultekinloveshisdogandcoding.com', ##not existent domain
            'port': 80,
            'timeout': 3,
            'blocking': True
        },
        {
            'name': 'Test 6: Blocking Mode Timeout (Unreachable Host)',
            'host': '10.255.255.1',
            'port': 80,
            'timeout': 3,
            'blocking': True
        }
    ]

    results = []

    for scenario in test_scenarios:
        print(f"\n### {scenario['name']} ###")
        result = change_settings(
            host=scenario['host'],
            port=scenario['port'],
            timeout=scenario['timeout'],
            blocking=scenario['blocking']
        )
        results.append({
            'scenario': scenario['name'],
            'success': result['success'],
            'error': result['error_type']
        })
    

    ##for test summary
    print("#"*54);
    print(" "*20 + " " + "TEST SUMMARY" +" " +" "*20);
    print("#"*54+"\n");
    for r in results:
        status = "TEST PASSED" if r['success'] or r['error'] else "TEST FAILED!!!"
        print(f"{r['scenario']}: {status}")
        if r['error']:
            print(f"  Error Type: {r['error']}")
    print("="*70)



if __name__ == "__main__":
    error_tests()
