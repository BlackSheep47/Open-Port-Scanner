import socket

MachineIp = input("Enter your machine Ip Address : ")

def check_port(MachineIp, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((MachineIp, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except socket.error:
        pass
    
def scan_ports(MachineIp):
    print(f"Scanning ports for {MachineIp}...")
    for port in range(1, 65535):
        check_port(MachineIp,port)
        
scan_ports(MachineIp)
        