#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ServiceException类"""

from .ExceptionCode import exceptioncode
from simutil.App import app


class ServiceException(Exception):
    __slots__ = ['errmsg', 'errno']

    def __init__(self, key=''):
        self.errmsg, self.errno = exceptioncode.get(key, (100000, 'system error'))

    def __str__(self):
        return "(code:{}, msg:{})".format(self.errno, self.errmsg)

    @staticmethod
    def handle(e: Exception):
        if isinstance(e, ServiceException):
            app('log').info(e.__str__())
        else:
            app('log').info(e.__str__())
