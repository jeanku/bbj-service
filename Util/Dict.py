#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""dict处理类"""

__author__ = ''


class Dict(object):
    _instance = None

    # Log为单例模式
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Dict, cls).__new__(cls, *args, **kw)
        return cls._instance

    # 返回dict1 和 dict2 交集key对应的dict2数据
    def intersection(self, dict1, dict2):
        inters = dict1.keys() & dict2.keys()
        return {index: dict2[index] for index in inters}

    # 返回在dict2中&不在dict1中的差集数据
    def difference(self, dict1, dict2):
        others = dict2.keys() - dict1.keys()
        return {index: dict2[index] for index in others}

    def to_string(self, data):
        if not data:
            return ''
        if isinstance(data, dict) or isinstance(data, list):
            return data.__str__()
        return data

    def items_to_string(self, data):
        return {index: self.to_string(value) for index, value in data.items()}


Dict = Dict()
