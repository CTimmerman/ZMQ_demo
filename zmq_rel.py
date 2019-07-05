import zmq


context = zmq.Context()

subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:9441")
subscriber.connect("tcp://127.0.0.1:9442")
subscriber.setsockopt(zmq.SUBSCRIBE, b"")
 
publisher = context.socket(zmq.PUB)
publisher.bind("tcp://127.0.0.1:9443")

while True:
	message = subscriber.recv()
	print("Relaying %r" % message)
	publisher.send(message)
