#import socket
import threading
import socketserver
import time
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow as tf

frames1=[]
# tf_frames1 = tf.constant([])
# tf_frames2 = tf.zeros([1024, 1024], tf.int32)
np_frames2 = np.zeros((1024,1024), dtype=int)
cnt=0

class ThreadedMyUDPHandler(socketserver.BaseRequestHandler): 
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        global frames1
        # global tf_frames1
        # global tf_frames2
        global np_frames2
        global cnt
        data=self.request[0].strip()
        data1=np.fromstring(data,dtype=int)
        # data1=int.from_bytes(data, byteorder="big", signed=False)
        np_frames2[cnt,:]=data1
        # tf_frames1=tf.concat([tf_frames1,data1],0)
        # frames1.extend(np.fromstring(self.request[0].strip(),dtype=np.int16))
        # socket = self.request[1]
        print("{} read: {}".format(self.client_address[0],"data"))
        print(np_frames2[cnt,:])
#        socket.sendto(data.upper(), self.client_address)
#        socket.sendto(data, self.client_address)
        # socket.sendto(bytes(self.client_address[0] + "\n", "utf-8"), self.client_address)
        
        # frames1.extend(data1)
        # print(len(frames1))
        cnt=cnt+1
        
        
class ThreadingUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass      


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = ThreadingUDPServer((HOST, PORT), ThreadedMyUDPHandler)
    with server:
        ip, port = server.server_address
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)
        
        try:
            while True: # keep alive
                pass
            
        except KeyboardInterrupt:
            server.shutdown()
            # global np_frames2
            # global cnt
            for i in range(cnt) :
                pass
                print(np_frames2[i,:])
            print("shutdown")
        
        # server.shutdown()