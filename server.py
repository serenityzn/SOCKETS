
#!/usr/bin/env python
import socket
import time
import thread
import sys
import os
# Custom import
import parser
import config

thread_count = 1
all_sockets = []
server_config = []

def communication(clsock, clip):
    res = 0
    message = clsock.recv(1024)
    if  message: 
        #clsock.send("Test socket server >" + message + "\n")
        print "<-RQUEST === [ " + str( message ) + " ]"
        
        ( request_lines, request_error_code ) = parser.get_lines( message )
        if request_error_code == 0:
            ( req_method, req_uri, req_http_ver ) = parser.get_main_params( request_lines[0] )
            if req_method == "HEAD":
                if os.path.exists(server_config["rootdir"] + req_uri) == True:
                    clsock.send(req_http_ver + " 200 OK\r\nServer: pserver/0.0.1\r\nContent-Length: 12\r\n\r\n")
                    print "-> RESPOND === [ " + req_http_ver + " 200 OK\r\nServer: pserver/0.0.1\r\nContent-Length: 12\r\n ]"
                else:
                    clsock.send(req_http_ver + "404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 17\r\n\r\nPage Not Found!\r\n")
                    print("-> RESPOND === [ " + req_http_ver + "404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 17\r\n\r\n")
            elif req_method == "GET":
                if os.path.exists(server_config["rootdir"] + req_uri) == True:
                    clsock.send(req_http_ver + " 200 OK\r\nServer: pserver/0.0.1\r\nContent-Length: 12\r\n\r\nHello World!\r\n")
                    print( "-> RESPOND === [ " + req_http_ver + " 200 OK\r\nServer: pserver/0.0.1\r\nContent-Length: 12\r\n\r\nHello World!\r\n ]" )
                else:
                    clsock.send(req_http_ver + "404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 17\r\n\r\nPage Not Found!\r\n")
                    print("-> RESPOND === [ " + req_http_ver + "404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 17\r\n\r\nPage Not Found!\r\n")

        if message[:5] == "/exit":
            clsock.close()
            res = 1
        elif message[:6] == "/trnum":
            print str( "Number of threads is: " + str( thread_count ) )
            clsock.send( "threads num is: " + str( thread_count) + "\n" )
        elif message[:7] == "/lssock":
            clsock.send( str(all_sockets) )
        elif message[:5] == "/help":
            clsock.send( "/exit - Exit\n/trnum - list number of threads\n/lssock - sockets list\n/help - Help"  )
    else:
        res = 1

    return res

def cl_socket_thread( thread_name, client_socket, client_address):
    global thread_count
    print "[" + thread_name + "]> Get connection from " + str(client_address) + "\n"
    #client_socket.send("Thank you for conneting to Test socket server! \n")
    #client_socket.send("Please enter your input.\n")
    while True:
        if client_socket:
            #print "THIS IS CLIENT SOCKET"
            #print " = " + str(client_socket)
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
    global server_config

    server_config = config.read_conf()

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
