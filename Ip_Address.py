# Write the code to print the Ip address of your system
import socket


def ip_adress():
    ip = socket.gethostbyname(socket.gethostname())
    return ip


print(ip_adress())
