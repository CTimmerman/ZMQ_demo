import time

import zmq


context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:9442")

while True:
	message = "Pub 2 says %s" % time.ctime()
	print("Sending %r" % message)
	publisher.send_string(message)
	time.sleep(1)
