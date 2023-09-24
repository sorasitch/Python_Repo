#import socket
import threading
import socketserver
import time

class ThreadedMyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote: {}".format(self.client_address[0],data))
#        print(data)
#        socket.sendto(data.upper(), self.client_address)
#        socket.sendto(data, self.client_address)
#        socket.sendto(bytes(self.client_address[0] + "\n", "utf-8"), self.client_address)
        
        
class ThreadingUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass      


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999
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
        
        # server.shutdown()