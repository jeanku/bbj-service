#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib


class ConfigParser():
    def __call__(self, module):
        module = module.split('.')
        m = importlib.import_module('{}'.format('.'.join(module[:-1])))
        return getattr(m, module[-1])


if __name__ == '__main__':
    data = ConfigParser()('Config.settings.Exchange_list')
    # data = ConfigParser()('settings.Symbol_name').get('USDT')               # read dict
    # data = ConfigParser()('settings.Exchange_list')[0]                      # read list
    print(data)
