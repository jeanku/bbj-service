#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""crontab 处理类"""

from .Parser import Parser
import importlib
import datetime
import time
from Exceptions.ServiceException import ServiceException


class Schedule(object):
    __slots__ = ['_path', '_import', '_classname', '_methodname']

    def __init__(self, path):
        self._path = path.split(':')
        temp = self._path[0].split('.')
        if temp[0] == 'Controller':
            self._import = '{}'.format('.'.join(temp[:-1]))
        else:
            self._import = 'Controller.{}'.format('.'.join(temp[:-1]))
        self._classname = temp[-1]
        self._methodname = self._path[1]

    def run(self):
        try:
            Import = importlib.import_module(self._import)
            importlib.reload(Import)
            classname = getattr(Import, self._classname)
            classname().__getattribute__(self._methodname)()
        except Exception as e:
            ServiceException.handle(e)

    def every_seconds(self):
        '''每秒钟运行一次'''
        return self

    def every_five_seconds(self):
        '''每5秒钟运行一次'''
        return self if datetime.datetime.now().second % 5 == 0 else None

    def every_ten_seconds(self):
        '''每10秒钟运行一次'''
        return self if datetime.datetime.now().second % 10 == 0 else None

    def every_thirty_seconds(self):
        '''每30秒钟运行一次'''
        return self if datetime.datetime.now().second % 30 == 0 else None

    def every_minutes(self):
        '''每分钟运行一次'''
        return self if datetime.datetime.now().second == 0 else None

    def every_five_minutes(self):
        '''每5分钟运行一次'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute % 5 == 0 else None

    def every_ten_minutes(self):
        '''每10分钟运行一次'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute % 10 == 0 else None

    def every_thirty_minutes(self):
        '''每30分钟运行一次'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute % 30 == 0 else None

    def daily(self):
        '''每天运行一次'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 else None

    def at(self, time):
        '''指定时间运行'''
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return self if time == now else None

    def weekly(self):
        '''每周运行一次'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.weekday() == 0 else None

    def monthly(self):
        '''每月运行一次'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.day == 1 else None

    def quarterly(self):
        '''每月运行一次'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.day == 1 and now.month % 4 == 0 else None

    def yearly(self):
        '''每月运行一次'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.day == 1 and now.month == 0 else None

    def weekdays(self):
        '''只在工作日运行任务'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.weekday() < 5 else None

    def sundays(self):
        '''每个星期天运行任务'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.weekday() == 6 else None

    def saturdays(self):
        '''每个星期六运行任务'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.weekday() == 5 else None

    def mondays(self):
        '''每个星期一运行任务'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.weekday() == 0 else None

    def tuesdays(self):
        '''每个星期二运行任务'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.weekday() == 1 else None

    def wednesdays(self):
        '''每个星期三运行任务'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.weekday() == 2 else None

    def thursdays(self):
        '''每个星期四运行任务'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.weekday() == 3 else None

    def fridays(self):
        '''每个星期五运行任务'''
        now = datetime.datetime.now()
        return self if now.second == 0 and now.minute == 0 and now.hour == 0 and now.weekday() == 4 else None

    def cron(self, cron):
        '''cron运行任务'''
        return self if Parser().parse(datetime.datetime.now(), cron) else None


if __name__ == '__main__':

    while (True):
        print(datetime.datetime.now().weekday(), " : ", Schedule('haha').cron('1-10,1-60/3 * * * * *'))
        time.sleep(1)
        # exit(0)
