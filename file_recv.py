import zmq
import time
import sys

count = 0
port = "5201"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    sink_file_content = socket.recv()
    print(count,":",len(sink_file_content))
    socket.send_string(str(len(sink_file_content)))
    sink_file = open(str(count)+"_rx.ge5", "wb")
    sink_file.write(sink_file_content)
    sink_file.close()
    #socket.send(len(sink_file_content))
    count += 1
