import sys, os
import logging
import logging.config
import inspect

config = 'hConf.config'
cur_folder=os.path.join(os.path.dirname(__file__),config)
logging.config.fileConfig(cur_folder)
mlog=logging.getLogger("root")

DEBUGMODE=os.getenv("DEBUG")

if DEBUGMODE == "1":
	mlog.warning("<DEBUGMODE ON>")
	mlog=logging.getLogger("debug")
	

debug = mlog.debug
info = mlog.info
warning = mlog.warning
error = mlog.exception
