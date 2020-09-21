#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Log日志类"""

__author__ = ''

import logging
import datetime
import os
from .Env import Env


class Log(object):
    _instance = None

    # Log为单例模式
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Log, cls).__new__(cls, *args, **kw)
            cls._add_log(cls._instance)
        return cls._instance

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def _add_log(self):
        dirname = os.path.dirname
        self.logger = logging.getLogger("logging")
        self.logger.setLevel("DEBUG")
        formatter = logging.Formatter('%(asctime)s 【%(levelname)s】%(message)s')
        fh = logging.FileHandler(Env().storage_path + "{}.log".format(datetime.datetime.now().strftime("%Y%m%d")))
        ch = logging.StreamHandler()
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        return self.logger
