import sys, os
import logging
import logging.config
import inspect

config = 'hConf.config'
cur_folder=os.path.join(os.path.dirname(__file__),config)
logging.config.fileConfig(cur_folder)

def debug(msg=None):
    logging.debug(msg)

def info(msg=None):
    logging.info(msg)

def warning(msg=None):
    logging.warning(msg)

def error(msg=None):
    logging.exception(msg)