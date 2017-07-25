import queue
import time
import pickle
import logging
import logging

try:
    import threading
except ImportError:
    import dummy_threading as threading

# === Base ATSOL Node ===

class BaseNode(threading.Thread):
    
    """
    BaseNode implements the common functionality of a node like
    start, link and stop different nodes and their corresponding Queues.
    """
    
    def __init__(self, name):
        
        """
        Initialize the thread and assign the BaseNode variables 
        """
        try:

             threading.Thread.__init__(self)
             self.name = name
             self._queue = queue.Queue()
          
        except:

             logging.error("Error: unable to start the thread")

    def run(self):

        """
        Create a thread and invoke the thread function 
        """
        try:
            logging.info("Starting " + self.name)
            self.process()
            logging.info ("Exiting " + self.name)
            
        except Exception as e:
            logging.error("Unable to run the " + self.name + " thread" + format(e))
        
        
    def stop(self):
        
        """
        This class method is to stop a thread  
        """
        self.join()
        
    def linkNode(self , obj):
        
        """
        Method to link itself to the next node
        """
        self.nextNode = obj
        
    def _insert(self, name):
        
        """
        Insert the data to the next node
        """
        try:
            self._queueLock.acquire()
            self.nextNode._queue.put(name)
            self._queueLock.release()
            logging.info("Inserted the data to " + name)
            
        except:
                
            logging.error("Error : insertion")
            
    def _get(self):

        """
        This method enables to get the data from the Queue
        """
        try:
           self._queueLock.acquire()
           if not self._queue.empty():
                d = self._queue.get(False)
                self._queueLock.release()
                return d

           else: 
                self._queueLock.release()
           return ""        
        except:
           self._queueLock.release()
           logging.error("unable to get the data")
        
    def isRunning(self):

        """
        This method is to check the thread status
        """
        return self._runnable
    
    def __str__(self):
        return self.name
    
    '''Queue and thread lock deceleration'''   
     
    _queueLock = threading.Lock()
    _runnable = True 
    
           
 
