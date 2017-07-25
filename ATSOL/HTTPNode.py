from BaseNode import BaseNode
import time
import queue
import urllib.request
import urllib.parse
import json
import http.client
import logging


# === HTTP Node ===

class HTTPNode(BaseNode):
    
    def __init__(self):
        
        """
        This class method is to initialize the thread and class variables  
        """
        name = "HTTPNode"
        BaseNode.__init__(self, name)
        self.name = name
        
        self.__httpServerIP = "192.168.55.5"
        self.__httpServerPort = 2020
        
    def __str__(self):
        return self.name
    
    def process(self):
        
        """
        This class method is to span and start a thread  
        """
        while self._runnable:
     
            try:
                
                self.__httpPost()
                time.sleep(1)
            except Exception as e:
                logging.error("__httpPost function failed "+ format(e))

    def __httpPost(self):
        
        """
        HTTP POST request
        """
        try:
            data = str(self._get())
            
            if len(data):
                logging.info("HTTP data: "+ data)
                
                try:    
                    tree_data = json.loads(data)
                except ValueError:
                    logging.error("Not a right JSON format")
                # URL encode the tree_data
              
                params = urllib.parse.urlencode(tree_data)
                
                headers = {"Content-type": "application/x-www-form-urlencoded",
                           "Accept": "text/plain"}
                
                conn = http.client.HTTPConnection(self.__httpServerIP,
                                                  self.__httpServerPort)
                conn.request("POST", "", params, headers)
                
                response = conn.getresponse()
                
                logging.info("HTTP Status: "+ str(response.status))
                logging.info("HTTP Reason" + str(response.reason))
                
                if response.status == 200:
                    self._insert("upload")
            else:
                time.sleep(1)
     
        except Exception as e:
            
            logging.error(self.name + format(e))
            raise