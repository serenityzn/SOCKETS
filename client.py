
#!/usr/bin/env python
import socket
import parser

def main():
#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 #   s.connect(("127.0.0.1", 1234))
    message = "GET/ HTTP/1.1\r\nSOME BODY\r\n"
    parser.get_lines(message)
    return 0

if __name__ == '__main__':
    main()
