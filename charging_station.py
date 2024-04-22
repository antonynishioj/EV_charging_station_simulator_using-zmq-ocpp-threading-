import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")

while True:
    request = input("Enter request (start_charging/stop_charging): ")
    if request == "start_charging":
        socket.send(b"start_charging")
    elif request == "stop_charging":
        socket.send(b"stop_charging")
    else:
        print("Invalid request")
        continue

    response = socket.recv()
    print(f"Received response: {response}")