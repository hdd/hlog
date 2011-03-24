import os,sys
import datetime
import logging
from pprint import pformat

class ConsoleInfoHandler(logging.StreamHandler):
    def __init__(self, *args, **kwargs):
        logging.StreamHandler.__init__(self, *args, **kwargs)

class GMAIL_SMTPHandler(logging.handlers.SMTPHandler):
    
    def emit(self, record):
        """
        Emit a record.

        Format the record and send it to the specified addressees.
        
        original code from 
        #http://mynthon.net/howto/-/python/python%20-%20logging.SMTPHandler-how-to-use-gmail-smtp-server.txt.
        """
        
        return 
        try:
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText

            import string # for tls add this line
            
            try:
                from email.utils import formatdate
            except ImportError:
                formatdate = self.date_time
                
            #    setup smtp
            port = self.mailport
            
            if not port:
                port = smtplib.SMTP_PORT
                
            smtp = smtplib.SMTP(self.mailhost, port)
            
            #    format the input message
            msg = self.format(record)
            
            #    get the file name
            filename = os.path.basename(record.pathname)
            
            logging.debug("getting script and system information...")
            
            #    start collecting the informations
            body={}
            body["FILENAME"]="%s"%filename
            body["USER"]="%s"%os.environ["USERNAME"]
            body["HOST"]="%s"%(os.environ["HOSTNAME"])
            body["FILE"]='<a href="file://%s">%s</a>'%(os.path.abspath(record.pathname),os.path.abspath(record.pathname))
            body["ARGS"]="None"
            body["DATETIME"]=datetime.datetime.now()
            body["PYTHONPATH"]="None"
            body["LOADEDMODULES"]="None"
            
            if len(sys.argv) > 1:
                body["ARGS"]=" ".join(sys.argv[1:])
            
            if "LOADEDMODULES" in os.environ:
                body["MODULES"]=("<br \>".join(os.environ["LOADEDMODULES"].split(":")))
            
            if "PYTHONPATH" in os.environ:
                body["PYTHONPATH"]=("<br \>".join(os.environ["PYTHONPATH"].split(":")))                
                
            body["PATH"]="<br \>".join(os.environ["PATH"].split(":"))
            body["SHELL"]="%s"%os.environ["SHELL"]
            body["PYTHON"]="%s"%sys.executable
            body["PYVERSION"]="%s"%sys.version
            body["MSG"]="%s"%("<br \>".join(msg.split(",")))
            
            #    generate a plain body text
            plain_body=[]
            for k,v in body.iteritems():
                plain_body.append("%s %s"%(k,v))
                
            plain_body="\n".join(plain_body)
                    
            #    fill the html with the collected data
            template=open(os.path.join(os.path.dirname(__file__),"template.html"),"r")
            html_body = str(template.read()).format(**body)

            #    define the email contents
            plain = MIMEText(plain_body, 'plain')
            html = MIMEText(html_body, 'html')
            
            #    set the email
            msg = MIMEMultipart('alternative')
            msg['Subject'] ="%s %s"%(self.getSubject(record),filename)
            msg['From'] = self.fromaddr
            
            #    we send back an email to the user 
            msg['To'] =",".join(self.toaddrs)
            
            #    fill the email content    
            msg.attach(plain)
            msg.attach(html)
            
            #    login to email account
            if self.username:
                smtp.ehlo() # for tls add this line
                smtp.starttls() # for tls add this line
                smtp.ehlo() # for tls add this line
                smtp.login(self.username, self.password)
            
            
            try:
                smtp.sendmail(self.fromaddr, self.toaddrs, msg.as_string())
            except:
                raise smtp.SMTPException , "EMAIL NOT SENT"
            
            smtp.quit()
            logging.warning("A Report Email is been sent to %s"%",".join(self.toaddrs))
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
