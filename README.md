## Network Diagnostic & Tool Package (NETDiagTP)

## About The Project

Network Diagnostic & Tool Package (NETDiagTP) is a Python application developed for network programming and diagnostics. This project demonstrates socket programming concepts, network tools and error management 

## Modules

### A - Machine Information
- Display hostname information
- Primary IP address detection (using special UDP trick on Linux systems)
- List all IP addresses
- Detailed logging support

### B - Echo Test
- **Echo Server**: Receive and echo back messages over TCP connection
- **Echo Client**: Send messages to server and receive responses
- Customizable port number (default: 56458)
- Success/failure verification
- Socket reuse support (SO_REUSEADDR)

### C - SNTP Time Sync
- Time synchronization with NTP servers (pool.ntp.org)
- Compare server time and local time
- Calculate time difference with millisecond precision
- NTPv3 protocol support

### D - Multi-Client Chat System
- **Chat Server**: 
  - Multiple client support
  - Concurrent connection management with threading
  - Message broadcast to all users
  - Username system
  - Connection/disconnection notifications
  - Crash prevention using "daemon" threads

- **Chat Client**:
  - Real-time messaging
  - Separate threads for sending and receiving messages
  - UTF-8 character support (Turkish Characters)

### D - Socket Settings
- Socket timeout configuration
- Send and Receive buffer size adjustment
- Blocking and Non-blocking mode selection
- Customizable host and port

### D-1 Error Management
Error scenarios and testing system:
- Connection Refused Error
- Timeout Error
- DNS Resolution Error
- Socket Error
- OS Error
- BlockingIOError
- Detailed error reporting and logging

##  Project Structure

```
network_diagnostic_and_tool_package/
│
├── main.py                          # Main application and menu system
├── README.md                        # This file
├── network_diagnostic.log           # Log file
│
└── modules/                         # Modules folder
    ├── a_machine_info.py            # Machine information module
    ├── c_sntp_time_sync.py          # SNTP time synchronization
    ├── e_error_management.py        # Error management and tests
    │
    ├── b_echo_test/                 # Echo test modules
    │   ├── echo_server.py           # Echo server
    │   └── echo_client.py           # Echo client
    │
    └── d_chat/                      # Chat modules
        ├── chat_server.py           # Chat server
        └── chat_client.py           # Chat client
```

##  Installation

### Requirements

- Python 3.6 or higher
- pip (Python package manager)

### Dependencies

 `ntplib` library

  an AUR helper like `yay`  or `paru` (only in arch-linux systems)

**Windows/Mac:**
```bash
pip install ntplib
```

**Linux (Ubuntu/Debian):**
```bash
pip install ntplib
```

**Arch Linux (using AUR):**
```bash
yay -S python-ntplib
```

##  Usage

### Starting the Application

```bash
python main.py
```

### Main Menu Options

```
###################################################
                    MAIN MENU                     
###################################################

1. Machine Information      # Display system information
2. Echo Test               # Start echo server/client
3. SNTP Time Check         # Check time synchronization
4. Chat                    # Start chat server/client
5. Socket Settings         # Test socket settings
6. Error Management        # Test error scenarios
0. Exit                    # Exit application
```

## Detailed Usage Examples

### Echo Test Usage

#### Starting the Server:
1. Select `2` from the main menu (Echo Test)
2. Select `1` (Start Echo Server)
3. Enter the port number you want (default: 56458)
4. Server will wait for connections

#### Starting the Client:
1. **Open a new terminal**
2. Select `2` from the main menu (Echo Test)
3. Select `2` (Start Echo Client)
4. Type the message you want to send
5. Enter the server port number
6. You will receive the echo response

### Chat System Usage

#### Starting Chat Server:
1. Select `4` from the main menu (Chat)
2. Select `1` (Start Chat Server)
3. Enter port number (default: 56458)
4. Server will wait for multiple client connections

#### Connecting Chat Client:
1. **Open new terminal(s)** (for multiple clients)
2. Select `4` from the main menu (Chat)
3. Select `2` (Start Chat Client)
4. Enter your username
5. Enter server host (for local: localhost)
6. Enter server port
7. Start chatting!

### Socket Settings Test

1. Select `5` from the main menu
2. Select `1` to test default settings, `2` for custom settings
3. For custom settings:
   - Host address (e.g., 8.8.8.8)
   - Port number (e.g., 53)
   - Timeout duration (seconds)
   - Blocking mode (1 = OFF, other = ON)

### Error Management Test

1. Select `6` from the main menu
2. Select `1` (Run Error Tests)
3. 6 different error scenarios will be automatically tested:
   - Connection Refused
   - Timeout
   - Successful Connection
   - Non-Blocking Mode
   - DNS Error
   - Unreachable Host

## Technical Details

### Python Modules Used

- **socket**: TCP/UDP network programming
- **threading**: Multi-threaded management (chat system)
- **logging**: Detailed log records
- **ntplib**: NTP protocol implementation
- **datetime**: Time operations
- **sys & os**: System operations

### Socket Programming Features

- **TCP (SOCK_STREAM)**: For Echo and Chat systems
- **UDP (SOCK_DGRAM)**: For Machine info IP detection
- **SO_REUSEADDR**: Port reuse support
- **Socket Timeout**: Connection timeout control
- **Buffer Management**: Send and Receive buffer settings
- **Blocking/Non-blocking**: Support for both modes

### Threading Structure

Threading structure used for chat system:
- **Daemon Threads**: Automatic termination when main program closes
- **Concurrent Handling**: Separate thread for each client
- **Thread Safety**: Safe message broadcasting

## Logging System

The application logs all operations to `network_diagnostic.log`:
- User actions
- Start/stop times
- Error messages
- Successful/failed operations

Log format:
```
[YYYY-MM-DD HH:MM:SS] Operation description
```

## Known Issues and Notes

### Linux IP Address Issue
- `socket.gethostbyname()` may return loop-back address on Linux (127.0.1.1)
- Solution: UDP socket connection trick to Google DNS (8.8.8.8) is used
- Alternative: `netifaces` library can be used (not currently included)

### Port Usage
- Default port: **56458**
- If port is busy, use a different port number
- Properly close the server with CTRL+C

### Firewall Warning
- Firewall permission may be required when running Chat and Echo servers
- Windows: Windows Defender will request permission
- Linux: Check `ufw` or `iptables` rules

##  Use Cases

### 1. Network Connectivity Test
- Test connections to different hosts using Socket Settings
- Observe timeout and error handling behaviors

### 2. LAN Chat System
- Set up a simple chat server on local network
- Chat with multiple clients
- Use for network troubleshooting

### 3. Time Synchronization Check
- Verify system time accuracy
- Understand NTP protocol
- Detect time difference problems

##  Debugging

### Server Won't Start
```bash
# Port might already be in use
# Solution: Use different port or check usage
netstat -ano | findstr :56458  # Windows
lsof -i :56458                  # Linux/Mac
```

### Client Can't Connect
- Make sure the server is running
- Verify you're using correct host and port
- Check firewall settings

### SNTP Not Working
- Check your internet connection
- Make sure `ntplib` is installed
- Check if firewall allows NTP traffic (port 123)

##  Developer Notes

### Code Structure
- Each module can work independently (standalone)
- Can be tested directly with `if __name__ == "__main__":`
- Modular

### Logging Levels
```python
logging.INFO    # General information messages
logging.WARNING # Warnings
logging.ERROR   # Errors
```

### Customization
All modules can be customized with parameters:
```python
# Example
echo_server(port=5000)
chat_server(host='0.0.0.0', port=8888)
change_settings(host='8.8.8.8', port=53, timeout=10)
```
### Final Notes
Feel free to contribute. Fork the repository and submit pull requests.

### SUPPORT FREE AND OPEN-SOURCE SOFTWARE



