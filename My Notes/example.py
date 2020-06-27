import socket
import sys
import threading
from queue import Queue
import time

host = input('\nEnter your target : ')
ip = socket.gethostbyname(host)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(2)
    try:
        con = s.connect_ex((ip, port))
        if con == 0:
            print('Port', port, 'is open!')
        con.close()
    except:
        pass


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

start = time.perf_counter()

q = Queue()

for worker in range(1,1000+1):
	q.put(worker)

for x in range(50):
	t = threading.Thread(target=threader)
	t.daemon = True
	t.start()

q.join()

end = time.perf_counter()
print('\nCompleted in {} seconds '.format(round(end - start, 2)))