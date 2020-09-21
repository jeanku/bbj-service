#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from simutil.App import app
import os


class BaseScript():

    def __init__(self):
        app.register("BASE_PATH", os.path.dirname(os.path.dirname(__file__)))

    def hello(self):
        print("parent hello")
