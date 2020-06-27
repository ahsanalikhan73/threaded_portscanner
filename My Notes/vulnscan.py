import os
import sys
import socket

def Banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return


def CheckVuln(filename, banner):
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line in banner:
                print('\nServer is Vulnerable to ' + banner)


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[0]
        if not os.path.isfile(filename):
            print('\nFile Doesnt Exitsts ')
            sys.exit(0)
        if not os.access(filename, os.R_OK):
            print('\nAccess Denied')

    else:
        print('\n[-] Usage : ' + sys.argv[0] + '<vuln Filename>')
        sys.exit(0)

    portlist = [21, 22, 23, 25, 80, 110, 443, 445]
    ip = '\n>> Enter Your Target IP : '

    for port in portlist:
        banner = Banner(ip, port)
        if banner:
            print('\n[+] ' + str(ip) + ' : ' + str(port) + '\t' + str(banner))
            CheckVuln(banner, filename)



if __name__ == '__main__':
    main()


