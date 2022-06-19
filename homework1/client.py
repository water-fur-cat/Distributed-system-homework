import pickle
import sys
import socket

if len(sys.argv) == 3:
    port = int(sys.argv[-2])
    message = str(sys.argv[-1])

elif len(sys.argv) == 2:
    port = int(sys.argv[-1])
    message = ["Empty","Message"] 

else:
    exit("Argument is wrong")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', port))

print('message to Server: {}\n'.format(message))
s.sendall(pickle.dumps(message))

data = pickle.loads(s.recv(1024))
print('Response from Server: {}\n'.format(data))
