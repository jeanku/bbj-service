#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Log日志类"""

__author__ = ''

import time
from Util.Libs.Log import Log


def clock(func):
    """统计方法执行的时间"""

    def clocked(*args, **kwargs):
        # pass
        start = time.perf_counter()
        result = func(*args, **kwargs)
        times = time.perf_counter() - start
        Log.info('[METHOD:TIME] %s.%s() : %0.8fs' % (func.__module__, func.__qualname__, times))
        return result
    return clocked


def trail(Log, Switch):
    def run(func):
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as e:
                Log.error(e, exc_info=Switch)

        return wrapper

    return run
