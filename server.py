
#!/usr/bin/env python
import socket
import time

def communication(clsock, clip):
    res = 0
    time.sleep(100)
    clsock.send("Test socket server >")
    message = clsock.recv(1024)
    clsock.send(message + "\n")
    if message[:5] == "\exit":
        clsock.close()
        res = 1 
    return res


def open_conn():
    listen_ip = "127.0.0.1"
    listen_port = 1234

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((listen_ip, listen_port))
    s.listen(2)

    (clientsocket, address) = s.accept()
    print "Got connection from",address
    clientsocket.send("Thank you for conneting to Test socket server! \n")
    clientsocket.send("Please enter your input.\n")

    while True:
        if communication(clientsocket, address) == 1:
            break

def main():
    open_conn()
    return 0

if __name__ == '__main__':
    main()
