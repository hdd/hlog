'''
this library collects all the configuration aspect of the logger


'''
import sys, os
import logging
import logging.config
import inspect

#    limit the objects
__all__ = ["get_config_path",
           "debug",
           "info",
           "error",
           "warning",
           "DEBUGMODE"]

#    default config file included

def get_config_path():
    '''
    search 
    '''
    if "LOG_CONFIG" in os.environ.keys():
        return os.environ["LOG_CONFIG_PATH"]
    else:
        cur_folder=os.path.dirname(__file__)
        logging.debug("lookging into local folder %s"%cur_folder)
        return os.path.join(cur_folder,'hConf.config')
    
    raise Exception , "No Config File Found, please set LOG_CONFIG_PATH"

#    setup the config file
config_file_path = os.path.join(get_config_path())
logging.config.fileConfig(config_file_path)
__mlog=logging.getLogger("root")

#    check for the DEBUG ENV , if it's set , enable the debug
DEBUGMODE=os.getenv("DEBUG")
if DEBUGMODE == "1":
    __mlog=logging.getLogger("debug")
    __mlog.debug("DEBUG MODE ON")
    

debug = __mlog.debug
info = __mlog.info
warning = __mlog.warning
error = __mlog.exception
