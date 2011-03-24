'''
this library collects all the configuration aspect of the logger


'''
import sys, os
import logging
import logging.config
import inspect

__all__ = ["get_config_path","debug","info","error","warning","DEBUGMODE"]

#    default config file included
_default_config_name = 'hConf.config'

def get_config_path():
    '''
    search 
    '''
    if "LOG_CONFIG" in os.environ.keys():
        return os.environ["LOG_CONFIG_PATH"]
    else:
        logging.warning("LOG_CONFIG environment variable not found")
        cur_folder=os.path.dirname(__file__)
        logging.debug("lookging into local folder %s"%cur_folder)
        return cur_folder
    
    raise Exception , "No Config File Found, please set LOG_CONFIG_PATH"

#    setup the config file
config_file_path = os.path.join(get_config_path(),_default_config_name)
logging.config.fileConfig(config_file_path)
mlog=logging.getLogger("root")

#    check for the DEBUG ENV , if it's set , enable the debug
DEBUGMODE=os.getenv("DEBUG")
if DEBUGMODE == "1":
    mlog.warning("<DEBUGMODE ON>")
    mlog=logging.getLogger("debug")
    

debug = mlog.debug
info = mlog.info
warning = mlog.warning
error = mlog.exception
