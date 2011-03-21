import sys, os
import logging
import logging.config
import inspect

config = 'hConf.config'
cur_folder=os.path.join(os.path.dirname(__file__),config)
logging.config.fileConfig(cur_folder)

debug = logging.debug
info = logging.info
warning = logging.warning
error = logging.exception