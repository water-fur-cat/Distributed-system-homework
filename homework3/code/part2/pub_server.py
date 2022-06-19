import zmq
import sys
import pickle
import socket

host=sys.argv[1]
port=str(sys.argv[2])
pub_port=str(sys.argv[3])

addr = 'tcp://' + host + ':' + port

context_post = zmq.Context()
post = context_post.socket(zmq.REP)
post.bind('tcp://{}:{}'.format(host, port))

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.bind('tcp://{}:{}'.format(host, pub_port))


while True:

    message = post.recv()
    post.send(message)
    data = pickle.loads(message)
    print('{}'.format(data))
    pub.send_string(data)
