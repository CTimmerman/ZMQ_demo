import zmq


context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:9443")
subscriber.setsockopt(zmq.SUBSCRIBE, b"")

while True:
	message = subscriber.recv()
	print("Received %r" % message)