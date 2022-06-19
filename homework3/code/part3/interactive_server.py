import zmq
import sys
import pickle
import time

host=sys.argv[1]
port=int(sys.argv[2])
pub_port=int(sys.argv[3])

context = zmq.Context()

receive = context.socket(zmq.REP)
receive.bind("tcp://{}:{}".format(host, port))

publish = context.socket(zmq.PUB)
publish.bind("tcp://{}:{}".format(host, pub_port))

while True:
    message = receive.recv()
    receive.send_string('')
    message = message.decode()
    print(message)

    publish.send_string(message)
    time.sleep(1)