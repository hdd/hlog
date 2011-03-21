import os,sys
import logging
from pprint import pformat

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
            
            filename = os.path.basename(record.pathname)
            #    TODO : CREATE HTML EMAIL
            body=[]
            body.append("USER:\n\t%s"%os.environ["USER"])
            body.append("HOSTNAME :\n\t%s"%(pformat(os.environ["HOSTNAME"])))
            
            if "LOADEDMODULES" in os.environ:
                body.append("MODULES:\n%s"%(pformat(os.environ["LOADEDMODULES"])))

            if "PYTHON_PATH" in os.environ:
                body.append("PYTHON PATH:\n\t%s"%os.environ["PYTHON_PATH"])
            
            body.append("PATH:\n%s"%(pformat(os.environ["PATH"].split(":"))))
            
            body.append(msg)
            body="\n\n".join(body)
            
            output_msg=[]
            output_msg.append("From :%s\r\n"%self.fromaddr)
            output_msg.append("To :%s\r\n"%string.join(self.toaddrs, ","))
            output_msg.append("Subject: %s %s\r\n"%(self.getSubject(record),filename))
            output_msg.append("Date: %s\r\n\r\n"%formatdate())
            output_msg.append("%s"%body)
            
            msg= "".join(output_msg)
            
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
    
    BLACK= (0,30)
    RED= (0,31)
    LRED= (1,31)
    
    GREEN= (0,32)
    LGREEN=(1,32)
    
    YELLOW=(0,33)
    LYELLOW=(1,33)
    
    BLUE=(0,34)
    MAGENTA=(0,35)
    
    CYAN=(0,36)
    LCYAN=(1,36)
    
    WHITE=(0,37)
    
    COLORS = {
        'WARNING'  : LYELLOW,
        'INFO'     : LGREEN,
        'DEBUG'    : LCYAN,
        'CRITICAL' : LYELLOW,
        'ERROR'    : LRED,
    }
        
    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[%d;%dm"
    
    def __init__(self, *args, **kwargs):
        # can't do super(...) here because Formatter is an old school class
        logging.Formatter.__init__(self, *args, **kwargs)

    def format(self, record):
        levelname = record.levelname
        
        text_color= self.COLOR_SEQ % self.COLORS[levelname]
        
        message   = logging.Formatter.format(self, record)
        message   = message.replace("$RESET", self.RESET_SEQ)\
                           .replace("$COLOR", text_color)
                             
        return message + self.RESET_SEQ
