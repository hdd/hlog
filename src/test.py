#!/usr/bin/env python

import os,sys

import hlog as log


log.debug("starting test.")

class MyTest(object):
    def __init__(self):
        log.debug("running init")
        for i in range(10):
            log.info("info mode")
                
    def print1(self):
        log.debug("running print 1")
        log.debug("debug mode")
        
    def print3(self):
        log.debug("print 3 , here we raise an exception")
        value = 0/0
        
    def print2(self):
        log.debug("running print 2")
        log.warning("warning mode")
        
        
class TestTest(MyTest):
    def __init__(self):
        log.debug("init subclass")
        super(TestTest,self).__init__()
        
        
T=TestTest()

try:
    T.print1()
    T.print2()
    T.print3()
except:
    log.error("Error found")
    
