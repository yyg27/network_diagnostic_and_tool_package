import sys
import os
from datetime import datetime

#importing modules
try:
    from modules.a_machine_info import get_machine_info
    from modules.c_sntp_time_sync import sntp_time_sync
    from modules.e_error_management import change_settings
except ImportError as e:
    print(f"Error importing modules: {e}");
    sys.exit(1);
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')#nt means windows

def print_header():
    #print(r"###"); r is for using raw-text
    print(r""" 
 _   _ _____ _____ ____  _            _____ ____  
| \ | | ____|_   _|  _ \(_) __ _  __ |_   _|  _ \ 
|  \| |  _|   | | | | | | |/ _` |/ _` || | | |_) |
| |\  | |___  | | | |_| | | (_| | (_| || | |  __/ 
|_| \_|_____| |_| |____/|_|\__,_|\__, ||_| |_|    
                                 |___/            """);


def print_footer():
    print("""                     
 ___.__.___.__. ____  
<   |  <   |  |/ ___\ 
 \___  |\___  / /_/  >
 / ____|/ ____\___  / 
 \/     \/   /_____/  
 """)

def print_menu():
    print("#"*51);
    print(" "*20 + " " + "MAIN MENU" +" " +" "*20);
    print("#"*51+"\n");
    print("1. Machine Information");
    print("2. Echo Test");
    print("3. SNTP Time Check");
    print("4. Chat");
    print("5. Socket Settings");
    print("6. Error Management");
    print("0. Exit");
    print("#"*51);

def machine_information_menu():
    clear_screen();
    print_header();

    try:
        info = get_machine_info();
        
        input("\nPress Enter to continue...");
    except Exception as e:
        print(f"Error: {e}");
        input("\nPress Enter to continue...");

def echo_test_menu():
    clear_screen();
    print_header();
    
    print("1 - Start Echo Server");
    print("2 - Start Echo Client");
    print("0 - Back to Main Menu");
    
    choice = input("\nEnter your choice: ").strip();
    
    if choice == '1':
        print("\nStarting Echo Server...");
        print("Note: Run the client in a separate terminal");
        try:
            from modules.b_echo_test.echo_server import echo_server;
            port = input("Enter port (default 56458): ").strip();
            port = int(port) if port else 56458;
            echo_server(port=port);
        except KeyboardInterrupt:
            print("\nServer stopped");
        except Exception as e:
            print(f"Error: {e}");
    
    elif choice == '2':
        print("\nStarting Echo Client...");
        try:
            from modules.b_echo_test.echo_client import echo_client;
            message = input("Enter message to echo: ").strip();
            if not message:
                message = "MARCO";
            port = input("Enter server port (default 56458): ").strip();
            port = int(port) if port else 56458;
            echo_client(message, port=port);
        except Exception as e:
            print(f"Error: {e}");
    
    input("\nPress Enter to continue...");

def sntp_time_menu():
    clear_screen();
    print_header();
    print("\n");
    
    try:
        sntp_time_sync();
        input("\nPress Enter to continue...");
    except Exception as e:
        print(f"Error: {e}")
        input("\nPress Enter to continue...");

def chat_menu():
    clear_screen();
    print_header();
    
    print("#"*57);
    print(" "*20 + " " + "CHAT MENU" +" " +" "*20);
    print("#"*57+"\n");
    print("1. Start Chat Server");
    print("2. Start Chat Client");
    print("0. Back to Main Menu");
    
    choice = input("\nEnter your choice: ").strip();
    
    if choice == '1':
        print("\nStarting Chat Server...");
        print("Note: Clients can connect from separate terminals");
        try:
            # Import here to avoid circular imports
            from modules.d_chat.chat_server import chat_server;
            
            port_input = input("Enter port (default 56458): ").strip();
            port = int(port_input) if port_input else 56458;
            
            chat_server(host='0.0.0.0', port=port);
            
        except KeyboardInterrupt:
            print("\nServer stopped");
        except Exception as e:
            print(f"Error: {e}");
            import traceback
            traceback.print_exc()
        
        input("\nPress Enter to continue...");
    
    elif choice == '2':
        print("\nStarting Chat Client...");
        try:
            from modules.d_chat.chat_client import chat_client
            
            host = input("Enter server host (default: localhost): ").strip();
            if not host:
                host = "localhost";
            
            port_input = input("Enter server port (default 56458): ").strip();
            port = int(port_input) if port_input else 56458;
            
            chat_client(host=host, port=port);
            
        except Exception as e:
            print(f"Error: {e}");
            import traceback;
            traceback.print_exc();
        
        input("\nPress Enter to continue...");
    
    elif choice == '0':
        return
    else:
        print("Invalid choice!")
        input("\nPress Enter to continue...")

def socket_settings_menu():
    clear_screen();
    print_header();

    print("#"*50);
    print(" "*20 + " " + "SETTINGS" +" " +" "*20);
    print("#"*50+"\n");

    print("Socket Settings");

    print("1. Test with default settings");
    print("2. Test with custom settings");
    print("0. Back to Main Menu");
    
    choice = input("\nEnter your choice: ").strip();
    
    try:
        if choice == '1':
            print("\nTesting with default settings...")
            change_settings();
        
        elif choice == '2':
            print("\nCustom Settings:");
            host = input("Host (default 8.8.8.8): ").strip() or '8.8.8.8';
            port = input("Port (default 53): ").strip();
            port = int(port) if port else 53;
            timeout = input("Timeout in seconds (default 5): ").strip();
            timeout = int(timeout) if timeout else 5;
            blocking_input = input("Set blocking mode on or off (Press 1 for switching OFF, else for ON),(default = ON): ");
            if blocking_input == "1":
                blocking = False
            else: 
                blocking = True
            
            change_settings(
                host=host,
                port=port,
                timeout=timeout,
                blocking=blocking
            );
        
        input("\nPress Enter to continue...");
        ##error handling
    except ValueError:
        print("Invalid input");
        input("\nPress Enter to continue...");
    except Exception as e:
        print(f"Error: {e}");
        input("\nPress Enter to continue...");

def error_management():
    clear_screen();
    print_header();

    print("1. Run Error Tests");
    print("0. Back to Main Menu");

    choice = input("\nEnter your choice: ").strip();
    
    if choice == '1':
        try:
            from modules.e_error_management import error_tests
            error_tests();#run tests
        except Exception as e:
            print(f"Error running tests: {e}");
        input("\nPress Enter to continue...");
    
    elif choice == '0':
        return
    
    else:
        print("Invalid choice");
        input("\nPress Enter to continue...");



##function to save logs to network_diagnostic.log file
def save_log(message):
    try:
        with open('network_diagnostic.log', 'a') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
            f.write(f"[{timestamp}] {message}\n");
    except:
        pass

def main():
    save_log("Application started");
    
    while True:
        clear_screen();
        print_header();
        print_menu();
        
        choice = input("\nEnter your choice: ").strip();
        
        if choice == '1':
            save_log("User selected: Machine Information");
            machine_information_menu();
        
        elif choice == '2':
            save_log("User selected: Echo Test");
            echo_test_menu();
        
        elif choice == '3':
            save_log("User selected: SNTP Time Sync");
            sntp_time_menu();
        
        elif choice == '4':
            save_log("User selected: Chat");
            chat_menu();
        
        elif choice == '5':
            save_log("User selected: Socket Settings");
            socket_settings_menu();
        
        elif choice == '6':
            save_log("User selected: Error Management")
            error_management();
        
        elif choice == '0':
            clear_screen();
            print_header();
            print("Exiting the app");
            print_footer();
            save_log("Application exited normally");
            sys.exit(0);
        
        else:
            print("\nInvalid choice");
            input("Press Enter to continue...");

if __name__ == "__main__":
    try:
        main();
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user");
        print("Exiting the app\n");
        print_footer();
        save_log("Application interrupted by user");
        sys.exit(0);
    except Exception as e:
        print(f"\nFatal error: {e}");
        save_log(f"Fatal error: {e}");
        sys.exit(1);