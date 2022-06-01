import socket
import sys
import time
import threading










print(r""" ____   ___  ____ _____   _   _ _   _ _   _ _____ _____ ____  
|  _ \ / _ \|  _ \_   _| | | | | | | | \ | |_   _| ____|  _ \ 
| |_) | | | | |_) || |   | |_| | | | |  \| | | | |  _| | |_) |
|  __/| |_| |  _ < | |   |  _  | |_| | |\  | | | | |___|  _ < 
|_|    \___/|_| \_\|_|   |_| |_|\___/|_| \_| |_| |_____|_| \_\
""")

print("\n*******************************************************")
print("\n*         Copyright of sidhanta palei,2022            *")
print("\n*      https://github.com/Sidhant0703/Port-hunter     *")
print("\n*******************************************************")


usage= "python3 port-hunter.py TARGET START_PORT-END_PORT"

if(len(sys.argv) !=4):
    print(usage)
    sys.exit()
try:
    target= socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()
start_port= int(sys.argv[2])
end_port= int(sys.argv[3])
start_time= time.time()

def scan_port(port):
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    conn= s.connect_ex((target, port))
    if(not conn):
        print("port", format(port), "is open")
    s.close()

    
for port in range(start_port, end_port+1):
    thread= threading.Thread(target = scan_port, args={port})
    thread.start()

end_time= time.time()
print("Time elapsed:", end_time-start_time)
