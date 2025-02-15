# -*- coding:utf-8 -*-
import os, os.path as osp
import time

def strftime(t = None):
    return time.strftime("%Y%m%d-%H%M%S", time.localtime(t or time.time()))

#################
# Logging
#################
import logging
logging.basicConfig(format="%(message)s")

DEFAULT_LEVEL = logging.INFO
DEFAULT_LOGGING_DIR = osp.join("logs", "Model")
fh = None

def init_fh():
    global fh
    if fh is not None:
        return
    if DEFAULT_LOGGING_DIR is None:
        return
    if not osp.exists(DEFAULT_LOGGING_DIR): os.makedirs(DEFAULT_LOGGING_DIR)
    logging_path = osp.join(DEFAULT_LOGGING_DIR, strftime() + ".log")
    fh = logging.FileHandler(logging_path)
    fh.setFormatter(logging.Formatter("%(message)s"))

def update_default_level(defalut_level):
    global DEFAULT_LEVEL
    DEFAULT_LEVEL = defalut_level

def update_default_logging_dir(default_logging_dir):
    global DEFAULT_LOGGING_DIR
    DEFAULT_LOGGING_DIR = default_logging_dir

def get_logger(name="CFXGB", level=None):
    level = level or DEFAULT_LEVEL
    logger = logging.getLogger(name)
    logger.setLevel(level)
    init_fh()
    if fh is not None:
        logger.addHandler(fh)
    return logger
