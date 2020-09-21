#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class AgentShorturlStatisticsModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'agent_shorturl_statistics'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 
        'token',                                                          # token
        'uid',                                                            # 这个token所属的UID
        'date',                                                           # 表示日期：20010203
        'location',                                                       # token触发的地点
        'lang',                                                           # 语言
        'num',                                                            # 计数
        'trade_btc',                                                      # 在这个token上注册的用户累计交易量BTC
        'rebate_btc',                                                     # 在这个token上注册的用户累计反佣BTC
        'update_time',                                                    # 更新时间
    ]