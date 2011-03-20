import logging

class InfoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.INFO

class DebugFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.DEBUG

class WarningFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.WARNING
    
class ErrorFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.ERROR    

class CriticalFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.CRITICAL      

class NotsetFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.NOTSET
       
class ErrorHandler(logging.StreamHandler):
    def __init__(self, *args, **kwargs):
        logging.StreamHandler.__init__(self, *args, **kwargs)
        #self.addFilter(NotsetFilter())
