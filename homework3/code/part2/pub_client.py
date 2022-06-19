import sys
import zmq
import pickle

host=sys.argv[1]
pub_port=int(sys.argv[2])

context = zmq.Context()
s = context.socket(zmq.SUB)
s.connect('tcp://{}:{}'.format(host,pub_port))
s.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    print(s.recv_string())