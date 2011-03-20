import os,sys
import hlog as log

class MyTest(object):
    def __init__(self):
        log.info("info mode","MyTest.__init__")
                
    def print1(self):
        log.debug("debug mode","MyTest.__init__")
        
    def print2(self):
        log.error("error mode","MyTest.__init__")
        
    def print3(self):
        log.warning("warning mode","MyTest.__init__")   

    def print4(self):
        log.critical("critical mode","MyTest.__init__")
        sys.exit(0)
         
M=MyTest()
M.print1()
M.print2()
M.print3()
M.print4()