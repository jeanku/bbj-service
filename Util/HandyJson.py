#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""HandyDict数据访问类"""

__author__ = ''

import json


class HandyJson(object):

    def __init__(self, data):
        if isinstance(data, str):
            self.__data = json.loads(data)
        else:
            self.__data = data

    def get(self, key, default=None):
        keys = key.split('.')
        data = self.__data
        for index in keys:
            if isinstance(data, dict):
                data = data.get(index, default)
            elif isinstance(data, list) and index.isdigit() and (0 <= int(index) < len(data)):
                data = data[int(index)]
            else:
                data = default
        return data

    def __getattr__(self, item):
        return self.get(item)



if __name__ == '__main__':
    #初始化
    data = '{"blockID": "0000","block_header": [{"raw_data": {"number": 41234, "txTrieRoot": "000","witness_address": "412ed","parentHash": "000","timestamp": 15300},"witness_signature": "f2b80fd00"}]}'
    data = HandyJson(data)

    print(data.get('block_header.0.raw_data.txTrieRoot', '444'))
