#!bin/python3
import socket
import sys
from datetime import datetime
if len(sys.argv) == 4:
    HOST=sys.argv[1]
    PORT_FROM,PORT_TO = int(sys.argv[2]),int(sys.argv[3])
    print(f"Started scanning the {HOST} at {datetime.now()}")
    try:
        for PORT in range(PORT_FROM,PORT_TO+1):
                s_connect = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                res = s_connect.connect_ex((HOST,PORT))
                if res == 0:
                    print(f"{PORT} port is opened")
                s_connect.close()
    except KeyboardInterrupt:
        print("Exciting program!!")
        sys.exit()
    except socket.gaierror:
        print("hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()
else:
    print("Error: Syntax must be ==> python3 portscanner.py <ip> <port_from> <port_to>")
