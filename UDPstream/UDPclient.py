import socket
import sys
import numpy as np

HOST, PORT = '192.168.1.39', 9999
#data = "data".join(sys.argv[1:])
data = "data"
amplitude=np.zeros([1024])+000
amplitude1=amplitude.tobytes()
print(len(amplitude))
print(len(amplitude1))
# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().

sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
#received = str(sock.recv(1024), "utf-8")
print("Sent:     {}".format(data))
print("Received: {}".format(received))

try:
    while True: # keep alive
        pass
#        sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
#        received = str(sock.recv(1024), "utf-8")
        sock.sendto(amplitude1, (HOST, PORT))
#        received = sock.recv(len(amplitude1))
#        sock.sendto(bytes(amplitude), (HOST, PORT))
#        received = sock.recv(len(bytes(amplitude)))
        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
    
    
except KeyboardInterrupt:
    sock.close()