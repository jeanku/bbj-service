#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""环境变量类"""

__author__ = ''

from configparser import ConfigParser
import os


class MyConfigParser(ConfigParser):
    """解决ConfigParser会将key名转成小写的问题"""

    def optionxform(self, str):
        return str


class Env(object):
    """Env主要是为了获取.env中的配置数据"""

    _base_path = str(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + '/'

    _instance = None

    _config = None

    _config_parser = None

    # Redis为单例模式
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Env, cls).__new__(cls, *args, **kw)
            cls._config_parser = MyConfigParser()
            cls._config_parser.read(cls._base_path + '.env')
            cls._config = dict(cls._config_parser.items('environment'))
        return cls._instance

    def __call__(self, name, defaule=''):
        return self._config.get(name, defaule)

    def __getattr__(self, name):
        return self._config.get(name)

    def items(self, key):
        return dict(self._config_parser.items(key))

    @property
    def base_path(self):
        """项目根目录"""
        return self._base_path

    @property
    def config_path(self):
        """项目配置目录"""
        return self._base_path + 'Config/'

    @property
    def controller_path(self):
        """项目django目录"""
        return self._base_path + 'Controller/'

    @property
    def storage_path(self):
        """项目log日志目录"""
        return self._base_path + 'Storage/'

    @property
    def util_path(self):
        """项目util库目录"""
        return self._base_path + 'Util/'


if __name__ == '__main__':

    env = Env()

    # 获取项目文件夹路径
    print("项目根目录:", env.base_path)
    print("log根目录:", env.storage_path)

    # 获取一般 .env配置
    print('获取当前环境:', env('ENVIRONMENT'))
    print('db host:', env('DB_HOST'))
    print('db name:', env('DB_NAME'))

    # 带默认值
    print('db host with default:', env('DB_HOST1', "127.0.0.1"))
    print('db name with default:', env('DB_NAME1', "jeanku"))

    # 按属性获取
    print('db name:', env.DB_NAME)
    print('db host:', env.DB_HOST)

    # 不存在的key 则返回None
    print('none key:', env.DB_NONE)

    # print("mobule config", env.items('evaluape_longhash'))
