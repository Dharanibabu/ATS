from FTPNode import FTPNode
from HTTPNode import HTTPNode
from UDPNode import UDPNode   

import socket
import sys
import logging
import logging.config

from builtins import str

if __name__ == '__main__':

    logging.config.fileConfig('logging.ini')

    # create logger
    logger = logging.getLogger('ATSOL')
    
    try:

        udp = UDPNode()
        http = HTTPNode()
        ftp = FTPNode()
        logger.info("Nodes created successfully")
    except:
        
        logger.error("Unable to create nodes")
 
    try:
        udp.linkNode(http)
        http.linkNode(ftp)
        logger.info("Nodes linked successfully : udp->http->ftp")
    except:
    
        logger.error("UDP to HTTP link node failure")
    try:    
        udp.start()     
        http.start()
        ftp.start()
        
        logger.info("Nodes are started")
        
        ftp.stop()
        http.stop()
        udp.stop()
        
        logger.info("Gracefully shutdowning the nodes")
        
        

    except:
        logger.error("Unable to start the nodes")
