#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from simutil.App import app
import os


class BaseScript:

    def __init__(self):
        app.register("BASE_PATH", os.path.dirname(os.path.dirname(__file__)))

    def log(self, data):
        if data.get('retCode', -1) == 0:
            app('log').info(self.uri + ': success, return:' + data.__str__())
        else:
            app('log').error(self.uri + ': error, return:' + data.__str__())
