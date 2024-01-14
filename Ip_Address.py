# Write the code to print the Ip address of your system
import socket


def ip_adress():
    # this are the predefined library of python
    ip = socket.gethostbyname(socket.gethostname())
    return ip


print(ip_adress())
