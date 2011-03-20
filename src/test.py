#!/usr/bin/env python

import os,sys
import hlog as log

class MyTest(object):
    def __init__(self):
        log.info("info mode")
                
    def print1(self):
        log.debug("debug mode")
        
    def print2(self):
        log.error("error mode")
        
    def print3(self):
        log.warning("warning mode")   

    def print4(self):
        log.critical("critical mode")
        sys.exit(0)

M=MyTest()
M.print1()
M.print2()
M.print3()
M.print4()
