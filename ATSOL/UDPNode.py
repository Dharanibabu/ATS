from BaseNode import BaseNode
import time
import queue
import socket
import logging
# === UDP Node ===

class UDPNode(BaseNode):
        
    def __init__(self):
        
        """
        This class method is to initialize the thread and class variables  
        """
        name = "UDPNode"
        BaseNode.__init__(self, name)
        self.__udpServerIP = "192.168.55.71"
        self.__udpServerPort = 8888
        self.__dataLength = 1024
        self.name = name
        
    def process(self):

        """
        This class method is to span and start a thread  
        """
        # Set up a UDP server
        try:
            UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        except:
            logging.error("UDP Socket creation failed")
        # Listen on port 21567
        # (to all IP addresses on this system)
        try:
            listen_addr = (self.__udpServerIP,self.__udpServerPort)
            UDPSock.bind(listen_addr)
            logging.info("UDP socket is listening to IP, Port - " + 
                         self.__udpServerIP + "," + format(self.__udpServerPort))
        except:
            logging.error("UDP Socket binding failed")
            
        while self._runnable:
            try:
                    
                data,addr = UDPSock.recvfrom(self.__dataLength)
     
                if not data: 
                    break
                
                reply = 'OK...' + str(data)

                print((addr[0]),str(addr[1])) 
                UDPSock.sendto(reply.encode(),addr)
                logging.info(str(data))
                self._insert(data.decode())
            
            except Exception as e:
                logging.error(forma(e))
