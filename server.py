
#!/usr/bin/env python
import socket
import time
import thread

thread_count = 1
all_sockets = []

def communication(clsock, clip):
    res = 0
#    clsock.send("Test socket server >")
    message = clsock.recv(1024)
    #clsock.send(message + "\n")
    print "<-RQUEST === [ " + str(message) + " ]"
    clsock.send("HTTP/1.0 200 OK\nServer: Test Web\nCache-Control: private\nContent-Type: text/html; charset=UTF-8\nLocation: http://127.0.0.1:1234\nContent-Length: 13\nDate: Thu, 25 Aug 2016 16:48:09 GMT\nConnection: close\n\nHello World!\n")
    print "->RESPOND " + str(flag)

    if message[:5] == "/exit":
        clsock.close()
        res = 1
    elif message[:6] == "/trnum":
        print str( "Number of threads is: " + str( thread_count ) )
        clsock.send( "threads num is: " + str( thread_count) + "\n" )
    elif message[:7] == "/lssock":
        clsock.send( str(all_sockets) )

    return res

def cl_socket_thread( thread_name, client_socket, client_address):
    global thread_count
    print "[" + thread_name + "]> Get connection from " + str(client_address) + "\n"
#    client_socket.send("Thank you for conneting to Test socket server! \n")
 #   client_socket.send("Please enter your input.\n")
    while True:
        if communication( client_socket, client_address ) == 1:
            thread_count -= 1
            break

def open_conn(ip, port, num):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind( ( ip, port ) )
    s.listen( num )

    return s

def main():
    global thread_count
    global all_sockets

    listen_ip = "127.0.0.1"
    listen_port = 1234
    number_connections = 2

    server_connection = open_conn( listen_ip, listen_port, number_connections )

    while True:
        (clientsocket, address) = server_connection.accept()
        print "up"
        all_sockets.append(clientsocket)
        try:
            thread.start_new_thread( cl_socket_thread, ( "Thread-"+str(thread_count), clientsocket, address, ) )
            thread_count += 1
        except:
            print "Failed to create thread"
            server_connection.close()
    return 0

if __name__ == '__main__':
    main()
