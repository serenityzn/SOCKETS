
#!/usr/bin/env python
import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 1234))
    return 0

if __name__ == '__main__':
    main()
