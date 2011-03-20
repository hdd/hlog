import sys, os
import logging
import logging.config
import inspect

config = 'hConf.config'
cur_folder=os.path.join(os.path.dirname(__file__),config)
logging.config.fileConfig(cur_folder)


def _set_msg(msg,libname):
    if libname:
        msg="[%s] %s"%(libname,msg)
    return msg

def debug(msg=None,libname=None):
    logging.debug(_set_msg(msg, libname))

def info(msg=None,libname=None):
    logging.info(_set_msg(msg, libname))

def warning(msg=None,libname=None):
    logging.warning(_set_msg(msg, libname))

def error(msg=None,libname=None):
    logging.error(_set_msg(msg, libname))
    
def critical(msg=None,libname=None):
    logging.critical(_set_msg(msg, libname))