import zmq
import time
import sys
import csv
from timeit import default_timer as timer

MAX_FILES = 1
SLEEP_TIME = 0

def send_file(src_file_name,req_socket):
    file_not_in_mem = timer()
    src_file = open(src_file_name,'rb')
    src_file_content = src_file.read()
    file_in_mem = timer()
    req_socket.send_pyobj(src_file_content)
    ack = req_socket.recv()
    # To-Do:Verify if correct size is received
    src_file.close()
    file_transferred = timer()
    file_transfer_time = file_transferred - file_not_in_mem
    stream_time = file_transferred - file_in_mem
    return [src_file_name,int(ack),round(file_transfer_time,6), round(stream_time,6)]

def main():
    port = "5201"

    if len(sys.argv) > 1:
        port =  sys.argv[1]
        int(port)

    stats_array = []
    stats_array.append(["Filename","Transfer Size","File Transfer Time","Stream Time"])
    context = zmq.Context()
    req_socket = context.socket(zmq.REQ)
    req_socket.connect("tcp://localhost:%s" % port)
    
    start_time = timer()
    for pref in range (0,MAX_FILES):
        file_name = str(pref)+".ge5"
        measures = send_file(file_name,req_socket)
        stats_array.append(measures)
        time.sleep(SLEEP_TIME)
    end_time = timer()
    
    print("Total Time Taken For Operation:",(end_time - start_time))
    result_file = open('result.csv', 'w')
    result = csv.writer(result_file)
    result.writerows(stats_array)
    result_file.close()

    req_socket.close()

if __name__=="__main__": 
    main()
