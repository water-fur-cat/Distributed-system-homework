import sys
import pickle
import datetime
import zmq
import time
import threading

def listen():
    while True:
        message = subscribe.recv().decode()
        print(message)
        time.sleep(1)
        
host=sys.argv[1]
port=int(sys.argv[2])
pub_port=int(sys.argv[3])
channel=sys.argv[4]
username=sys.argv[5]

print('{} Channel'.format(channel))

context = zmq.Context()

post = context.socket(zmq.REQ)
post.connect("tcp://{}:{}".format(host, port))

subscribe = context.socket(zmq.SUB)
subscribe.connect("tcp://{}:{}".format(host, pub_port))

subscribe.setsockopt_string(zmq.SUBSCRIBE, '({})'.format(channel))
if channel == 'ALL':
    subscribe.setsockopt_string(zmq.SUBSCRIBE, '')

t = threading.Thread(target=listen)
t.start()

while True:
    input_message = sys.stdin.readline().strip('\n')
    send_message = '({}) {}: {} ({})'.format(channel, username, input_message, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    post.send_string(send_message)
    post.recv()