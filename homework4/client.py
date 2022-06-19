import collections
import requests
import hashlib
import sys
import threading
import string
import queue
import os
import time
import pprint

def request(hashed_password, partition, length, worker, port):
    try:
        r = requests.get(url="http://127.0.0.1:{}/passwordcracker".format(port), json={"password": hashed_password,"partition": partition,'length': length})
    except requests.exceptions.ConnectionError:
        del jobs[worker]
        del ports[worker]
        return

    data = r.text
    if data != 'Cannot crack it.':
        print(data)

    if data != 'Cannot crack it.':
        end = round(time.time()-start,4)
        answer = {"time": '{} s'.format(end)}
        pprint.pprint(answer)
        os._exit(1)

threads = int(sys.argv[1])
password = sys.argv[2]                                                                                                                
max_length = int(sys.argv[3])                                                      
hashed_password = hashlib.md5(password.encode()).hexdigest()                    
start = time.time()                                                             
ports = ['500{}'.format(i) for i in range(threads)]                             

if __name__ == '__main__':
    # letters = collections.deque()
    letters = queue.Queue()
    for i in string.printable:
        letters.put(i)

    # for i in string.ascii_lowercase:
    #     letters.append(i)

    jobs = []
    for i in range(threads):
        # partition = letters.popleft()
        partition = letters.get()
        t = threading.Thread(target=request, args=(hashed_password, partition, max_length, i, ports[i]))
        t.daemon = True
        jobs.append(t)
        t.start()

    while True:
        if not letters:
            os._exit(1)

        for i,j in enumerate(jobs):
            if j.is_alive():
                continue
            else:
                # partition = letters.popleft()
                partition = letters.get()
                worker = i
                port = ports[i]
                t = threading.Thread(target=request, args=(hashed_password, partition, max_length, worker, port))
                t.daemon = True
                jobs[i] = t
                t.start()