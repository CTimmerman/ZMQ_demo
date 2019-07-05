import time

import zmq


context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:9441")

while True:
	message = "Pub 1 says %s" % time.ctime()
	print("Sending %r" % message)
	publisher.send_string(message)
	time.sleep(1)
