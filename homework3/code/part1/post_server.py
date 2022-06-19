import zmq
import sys
import pickle

host=sys.argv[-2]
port=str(sys.argv[-1])

addr = 'tcp://' + host + ':' + port
# print(addr)
context = zmq.Context()
s = context.socket(zmq.REP)
s.bind(addr)

while True:
    message = s.recv()
    s.send(message)
    data = pickle.loads(message)
    print('{}'.format(data))
    