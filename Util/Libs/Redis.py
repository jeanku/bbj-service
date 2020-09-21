#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""redis数据访问类"""

__author__ = ''

import redis
from .Env import Env


class Redis(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            env = Env()
            pool = redis.ConnectionPool(host=env("REDIS_HOST"), port=env("REDIS_PORT"), db=env("REDIS_DBID"),
                                        password=env('REDIS_PASSWORD', None), decode_responses=True)
            cls._instance = redis.Redis(connection_pool=pool)
        return cls._instance


if __name__ == '__main__':
    # 建议用实例Redis处理数据Redis.get("key1")， 而不是Redis().get("key1")
    # string demo
    # print(app('redis'))
    # exit(0)
    print(Redis().set("key1", "value1"))
    print(Redis().get("key1"))

    # list demo
    # print(Redis.lpush("key2", "value1"))
    # print(Redis.lpush("key2", "value2"))
    # print(Redis.lpop("key2"))
