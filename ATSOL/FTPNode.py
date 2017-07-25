from BaseNode import BaseNode
import time
import queue
from ftplib import FTP
import logging

# === FTP Node ===

class FTPNode(BaseNode):
    
    #_queue = queue.Queue()
        
    def __init__(self):
        
        """
        This class method is to initialize the thread and class variables  
        """
        name = "FTPNode"
        BaseNode.__init__(self,name)
        self.name = name
        
        #FTP server login credentials
        
        self.__ftpServerIP = "192.168.55.128"
        self.__ftpServerPort = 2122
        self.__ftpServerLogin = "user"
        self.__ftpServerPass = "we1c@me"
    
    def __str__(self):
        return self.name
        
    def process(self):
        
        """
        This class method is to span and start a thread  
        """
        while self._runnable:
            try:
              #  print("FTPNode Inserting")
                if self._get():
                        
                    data = "FTPNode"# + str(time.ctime(time.time()))
                    #self._insert(data)
                    self.__uploadFile()
                    time.sleep(1)
                else:
                    time.sleep(2)
                        
            except Exception as e:
                logging.error(format(e))
                time.sleep(5)
            
    def __uploadFile(self):

        """
        This module enable to establish a ftp connection and uplod the image to 
        the respective folder in a ftp server
        """
                
        try:
            fh = open("Tulips.jpg", 'rb')
            
            # Connect to an FTP test server
            try:
                ftp = FTP()
                connStatus = ftp.connect(self.__ftpServerIP,self.__ftpServerPort)
                logging.info("Connected successfully " + connStatus)
            except:
                logging.error("FTP connection error")
                return
            # Login to the server
            
            reply = ftp.login(self.__ftpServerLogin, self.__ftpServerPass)
                
            logging.info(self.name + 'FTP login reply:' + format(reply))
    
            # Change to the proper directory for upload
            #ftp.cwd('/dharani/')
    
            # Open the file and upload it to the server
            reply = ftp.storlines('STOR '+ self.name + '.jpg', fh)
            logging.info(self.name + " "+ format(reply))
    
        except Exception as e:
            logging.error(format(e))
            raise
    
        finally:
            if fh:
                fh.close()
        