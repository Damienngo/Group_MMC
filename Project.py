import socket

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Please enter the IP address that you want to Scan: ")
port = int(input("Please enter the port you want to Scan: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The Port is open")

portScanner(port)
