import os,sys
import logging

class ConsoleInfoHandler(logging.StreamHandler):
    def __init__(self, *args, **kwargs):
        logging.StreamHandler.__init__(self, *args, **kwargs)
        
        if os.environ.has_key("DEBUG"):
            self.setLevel(logging.DEBUG)

class GMAIL_SMTPHandler(logging.handlers.SMTPHandler):
    def emit(self, record):
        """
        Emit a record.

        Format the record and send it to the specified addressees.
        
        original code from 
        #http://mynthon.net/howto/-/python/python%20-%20logging.SMTPHandler-how-to-use-gmail-smtp-server.txt.
        """
        try:
            import smtplib
            import string # for tls add this line
            try:
                from email.utils import formatdate
            except ImportError:
                formatdate = self.date_time
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port)
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
                            self.fromaddr,
                            string.join(self.toaddrs, ","),
                            self.getSubject(record),
                            formatdate(), msg)
            if self.username:
                smtp.ehlo() # for tls add this line
                smtp.starttls() # for tls add this line
                smtp.ehlo() # for tls add this line
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


class ColorFormatter(logging.Formatter):
    
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
    
    COLORS = {
        'WARNING'  : YELLOW,
        'INFO'     : WHITE,
        'DEBUG'    : BLUE,
        'CRITICAL' : YELLOW,
        'ERROR'    : RED,
    }
    
    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[1;%dm"
    
    def __init__(self, *args, **kwargs):
        # can't do super(...) here because Formatter is an old school class
        logging.Formatter.__init__(self, *args, **kwargs)

    def format(self, record):
        levelname = record.levelname
        color     = self.COLOR_SEQ % (30 + self.COLORS[levelname])
        message   = logging.Formatter.format(self, record)
        message   = message.replace("$RESET", self.RESET_SEQ)\
                           .replace("$COLOR", color)
        for k,v in self.COLORS.items():
            message = message.replace("$" + k,    self.COLOR_SEQ % (v+30))\
                             .replace("$BG" + k,  self.COLOR_SEQ % (v+40))\
                             .replace("$BG-" + k, self.COLOR_SEQ % (v+40))
        return message + self.RESET_SEQ
