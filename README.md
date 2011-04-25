hlog
=============

Born as reseach on the python logging system, 
hlog is an "almost configured" logging python module, which permits to have:

* easy debug mode switch
* color output for all the configuration
* in case of exception an email will be sent to the destination address listed in the config file
* debug mode disable the email and redirect it to the standard output

to use it
---
just include the folder in your PYTHONPATH env:

`import sys ; sys.path.insert(0,<path to the hlog source folder>)`

