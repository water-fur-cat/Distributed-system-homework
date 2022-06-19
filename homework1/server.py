import socket 
import sys
import pickle

if len(sys.argv) == 3:
    port = int(sys.argv[-2])
    message = str(sys.argv[-1])

elif len(sys.argv) == 2:
    port = int(sys.argv[-1])
    message = {"Hello":"Empty", "World":"message"}
else:
    exit("Too many arguments")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', port))
print('Listening...\n')
s.listen(1)
connection, client_addr = s.accept()

data = pickle.loads(connection.recv(1024))
print('Message from Client: {}\n'.format(data))

print('Response to Client: {}'.format(message))
connection.sendall(pickle.dumps(message))


