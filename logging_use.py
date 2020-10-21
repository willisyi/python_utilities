#! /usr/env python
# refer: https://blog.csdn.net/momoyaoquaoaoao/article/details/87280440
import os,sys
import logging

def logging_config(loglevel, logfile):
    # Configure the logging log level and output it to the console.
    logging.basicConfig(level=loglevel,
            format='[%(asctime)s][%(levelname)s]%(message)s',
            datefmt="%d %b %Y %H:%M:%S",
            filename=logfile, filemode="w")

    # config logging output to the console
    console = logging.StreamHandler()
    console.setLevel(loglevel)
    formatter = logging.Formatter("[%(levelname)s] %(message)s")
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    
    
if __name__ == "__main__":
    
    # Test logging_config
    logging_config(logging.DEBUG, "test.log")
    logging.debug("This is debug info")

    logging.info("This is the test for logging info")
    logging.error("This is the test for logging error")
    
