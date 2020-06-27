
import socket

def Banner(ip, port):
    socket.setdefaulttimeout(1)
    try:
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(2024)
        return banner
    except:
        return

def main():
    ip = input('\nEnter your Target IP : ')
    # port = 53
    for port in range(100):
        banner = Banner(ip, port)
        if banner:
            print('\n[+] ' + str(ip) + ' : ' + str(port) + '\t' + str(banner))


if __name__ == '__main__':
    main()
