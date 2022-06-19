import zmq
import sys
import pickle
import datetime

host=sys.argv[1]
port=str(sys.argv[2])
username=sys.argv[3]
message=' '.join(sys.argv[4:])
addr = 'tcp://' + host + ':' + port

send_message = '{}: {} ({})'.format(username, message, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

context = zmq.Context()
s = context.socket(zmq.REQ)
s.connect(addr)
# print(send_message) 
s.send(pickle.dumps(send_message))
print(pickle.loads(s.recv()))
