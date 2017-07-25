from FTPNode import FTPNode
from HTTPNode import HTTPNode
from UDPNode import UDPNode   
from BaseNode import BaseNode


import logging
import logging.config

import unittest

class TestAtsol(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
    
    def test_getName(self):
        ftp = FTPNode()
        self.assertEqual(ftp.__str__(),"FTPNode")
    
    def test_httpNode(self):
        http = HTTPNode()
        self.assertEqual(http.__str__(),"HTTPNode")
        
if __name__ == '__main__':
    unittest.main()
    
