
# Make a Threaded Port Scanner
from socket import *
from argparse import *
from sys import exit, argv
from threading import *
from queue import Queue
import time

class Port_Scanner():

    def __init__(self):
        self.q = Queue()
        # self.s = socket(AF_INET, SOCK_STREAM)

    def connect(self, t_host, tport):
        s = socket(AF_INET, SOCK_STREAM)
        if tport:
            try:
                res = s.connect_ex((t_host, tport))
                # self.s.connect((t_host, tport))
                if res == 0:
                    print('[+] Port ' + str(tport) + ' is Open')
            except:
                # print('[+] Port ' + str(tport) + ' is Closed')
                pass
            finally:

                # self.s.close()
                s.close()


    def connScan(self, t_host, tport):
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(1)
        try:
            s.connect((t_host, tport))
            # self.s.connect((t_host, tport))
            print('[+] Port ' + str(tport) + ' is Open')
        except:
            print('[+] Port ' + str(tport) + ' is Closed')
        finally:
            # self.s.close()
            s.close()

    def port_range_thread(self, host, port):
        s = socket(AF_INET, SOCK_STREAM)
        setdefaulttimeout(2)
        try:
            # con = self.s.connect_ex((self.host, port))
            con = s.connect_ex((host, port))
            if con == 0:
                print('Port', port, 'is open!')
        except:
            pass
        finally:
            # self.s.close()
            s.close()

    def threader(self, host):
        while True:
            worker = self.q.get()
            self.connect(host, worker)   # here worker is the port
            self.q.task_done()


    def port_scan(self, t_host, tport, port_range):
        try:
            target = gethostbyname(t_host)
        except:
            print('\n[!] Unknown Host ' + t_host)
            exit(0)

        print('\n[+] Scan Results for : ' + target + '\n')

        if port_range:
            split_ports = port_range.split('-')

            for worker in range(int(split_ports[0]), int(split_ports[1])):
                self.q.put(worker)

            for x in range(50):
                t = Thread(target=self.threader, args=[t_host])
                t.daemon = True
                t.start()

            self.q.join()

        else:
            for p in tport:
                t = Thread(target=self.connect, args=(t_host, int(p)))
                t.start()
                t.join()


    def arguments(self):
        parser = ArgumentParser()
        parser.add_argument('-t', '--target', dest='target', help='Specify Host IP / Address')
        parser.add_argument('-p', '--port', dest='port', help='Specify The Port To Scan')
        parser.add_argument('-pr', '--port-range', dest='pr', help='Specify The Range Of Ports To Scan')
        values = parser.parse_args()

        if not values.target:
            parser.error('\n\n[-] Please Specify The Target Host IP\n')

        if len(argv) == 3:
            print('\n[*] Didn\'t Spcify Any Port(s) To Scan ...\n')
            print(' >>> Usage: python3 ' + argv[0] + ' -t < Host > -p(r) < Range | Number of Ports > \n')
            exit(0)

        host = values.target
        tport = str(values.port).split(',')
        port_range = values.pr

        self.port_scan(host, tport, port_range)         # function call

    def main(self):
        start = time.perf_counter()
        self.arguments()
        end = time.perf_counter()
        print('\nCompleted in {} seconds \n'.format(round(end - start, 2)))

if __name__ == '__main__':
    scanner = Port_Scanner()
    scanner.main()