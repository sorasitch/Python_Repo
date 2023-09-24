import socket
import sys
import numpy as np

# HOST, PORT = "192.168.1.39", 9999
# HOST, PORT = "172.0.0.1", 9999
HOST, PORT = "localhost", 9999
#data = "data".join(sys.argv[1:])


fs = 44100
N = 2048 * 200#10*fs
# nperseg = 512
amp = 15000
noise_power = 0.001 * fs / 2
time = np.arange(N) / float(fs)
carrier = amp * np.sin(2*np.pi*time*2500)
carrier1 =  amp * np.sin(2*np.pi*time*5000)
carrier2 =  amp * np.sin(2*np.pi*time*15000)
noise = np.random.normal(scale=np.sqrt(noise_power),
                         size=time.shape)
x = (carrier + noise) + carrier1 + carrier2
x = x.astype(dtype=int)
num_loop = int (N / 1024)


data = "data"
# amplitude=x #np.zeros([1024])+1000
# amplitude1=amplitude.tobytes()
# print(len(amplitude))
# print(len(amplitude1))
# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().

# sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
#received = str(sock.recv(1024), "utf-8")
# print("Sent:     {}".format(data))
# print("Received: {}".format(received))

try:
        i=0
        while True: # keep alive
                pass
                if i > 1 : break
                amplitude=x[(i*1024):(i+1)*1024]
                amplitude1=amplitude.tobytes()
                # amplitude1=bytes(amplitude, "int")
        #        sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
        #        received = str(sock.recv(1024), "utf-8")
                sock.sendto(amplitude1, (HOST, PORT))
        #        received = sock.recv(len(amplitude1))
        #        sock.sendto(bytes(amplitude), (HOST, PORT))
        #        received = sock.recv(len(bytes(amplitude)))
                print("Sent:     {} , {} ".format(data,i))
                print(amplitude)
                # print("Received: {}".format(received))
                i=i+1
    
    
except KeyboardInterrupt:
        sock.close()
