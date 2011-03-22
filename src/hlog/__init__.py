import sys, os
import logging
import logging.config
import inspect

config = 'hConf.config'
cur_folder=os.path.join(os.path.dirname(__file__),config)
logging.config.fileConfig(cur_folder)

if "DEBUG" in os.environ:
	mlog=logging.getLogger("debug")
else:
	mlog=logging.getLogger("root")

debug = mlog.debug
info = mlog.info
warning = mlog.warning
error = mlog.exception
