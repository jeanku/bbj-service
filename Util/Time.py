#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""json数据访问类"""

__author__ = ''

import time


class Time(object):

    @staticmethod
    def date(format, timestr):
        # %Y-%m-%d %H:%M:%S
        return time.strftime(format, time.localtime(timestr))

    @staticmethod
    def time():
        return int(time.time())

    @staticmethod
    def strtotime(timestr, format):
        '''
        时间格式转时间戳
        :param timestr: 2019-10-20 13:45:58
        :param format:  %Y-%m-%d %H:%M:%S
        :return:
        '''
        return int(time.mktime(time.strptime(timestr, format)))

