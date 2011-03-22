#!/usr/bin/env python

import os,sys
import hlog as log

class MyTest(object):
    def __init__(self):
	for i in range(10):
        	log.info("info mode")
                
    def print1(self):
        log.debug("debug mode")
        
    def print2(self):
        try:
            0/0
        except:
            log.error("critical Error")
        
    def print3(self):
        log.warning("warning mode")
        
        
class TestTest(MyTest):
    def __init__(self):
        super(TestTest,self).__init__()
    
    
T=TestTest()
T.print1()
T.print3()
T.print2()
