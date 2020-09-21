#!/usr/bin/python
# -*- coding: UTF-8 -*-

from simpysql.DBModel import DBModel
import os


class BaseModel(DBModel):
    __basepath__ = os.path.dirname(os.path.dirname(__file__)) + '/'



