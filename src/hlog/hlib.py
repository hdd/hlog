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
       
class ConsoleErrorHandler(logging.StreamHandler):
    def __init__(self, *args, **kwargs):
        logging.StreamHandler.__init__(self, *args, **kwargs)

class ConsoleInfoHandler(logging.StreamHandler):
    def __init__(self, *args, **kwargs):
        logging.StreamHandler.__init__(self, *args, **kwargs)
        

class ColorFormatter(logging.Formatter):
    
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
    
    COLORS = {
        'WARNING'  : YELLOW,
        'INFO'     : WHITE,
        'DEBUG'    : BLUE,
        'CRITICAL' : YELLOW,
        'ERROR'    : RED,
        'RED'      : RED,
        'GREEN'    : GREEN,
        'YELLOW'   : YELLOW,
        'BLUE'     : BLUE,
        'MAGENTA'  : MAGENTA,
        'CYAN'     : CYAN,
        'WHITE'    : WHITE,
    }
    
    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[1;%dm"
    BOLD_SEQ  = "\033[1m"
    
    def __init__(self, *args, **kwargs):
        # can't do super(...) here because Formatter is an old school class
        logging.Formatter.__init__(self, *args, **kwargs)

    def format(self, record):
        levelname = record.levelname
        color     = self.COLOR_SEQ % (30 + self.COLORS[levelname])
        message   = logging.Formatter.format(self, record)
        message   = message.replace("$RESET", self.RESET_SEQ)\
                           .replace("$BOLD",  self.BOLD_SEQ)\
                           .replace("$COLOR", color)
        for k,v in self.COLORS.items():
            message = message.replace("$" + k,    self.COLOR_SEQ % (v+30))\
                             .replace("$BG" + k,  self.COLOR_SEQ % (v+40))\
                             .replace("$BG-" + k, self.COLOR_SEQ % (v+40))
        return message + self.RESET_SEQ
