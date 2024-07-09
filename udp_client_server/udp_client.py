import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5000
MESSAGE_SIZE = 64

MESSAGE = b"A"*MESSAGE_SIZE

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("Message Size: %d" % MESSAGE_SIZE)
print("Message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
