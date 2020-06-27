
from socket import *
from argparse import *
from sys import exit

def arguments():
    parser = ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Specify Host IP / Address')
    parser.add_argument('-p', '--port', dest='port', help='Specify the port to scan')
    parser.add_argument('-pr', '--port-range', dest='pr', help='Specify the range of ports to scan')

    values = parser.parse_args()
    if not values.target:
        parser.error('\n\n\t[-] Please specify the target host ip\n')

    return values

def main():
    options = arguments()       # function call
    try:
        target = gethostbyname(options.target)
    except:
        print('\n[!] Unknown Host ' + options.target)
        exit(0)

    try:
        target_name = gethostbyaddr(target)
        print('\n[+] Scan Results for : ' + target_name[0])
    except:
        print('\n[+] Scan Results for : ' + target + '\n')


    # make actual function to scan
    port = options.port         # takes single port to scan
    port_range = options.pr     # takes port range to scan

    if port:
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(1)
        result = s.connect_ex((target, int(options.port)))
        if result == 0:
            print('[+] Port ' + str(options.port) + ' is Open ...!\n')
        else:
            print('[+] Port ' + str(options.port) + ' is Closed ...!\n')
        s.close()

    elif port_range:
        split_ports = port_range.split('-')
        for x in range(int(split_ports[0]), int(split_ports[1])):
            s = socket(AF_INET, SOCK_STREAM)
            setdefaulttimeout(1)
            result = s.connect_ex((target, x))
            if result == 0:
                print('[+] Port ' + str(x) + ' is Open ...!')
            s.close()

    else:
        for x in range(1,1000+1):
            s = socket(AF_INET, SOCK_STREAM)
            setdefaulttimeout(1)
            result = s.connect_ex((target, x))
            if result == 0:
                print('[+] Port ' + str(x) + ' is Open ...!')
            s.close()


if __name__ == '__main__':
    main()