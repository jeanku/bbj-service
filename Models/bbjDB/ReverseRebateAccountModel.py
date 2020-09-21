#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class ReverseRebateAccountModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'reverse_rebate_account'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                              # 自增ID
        'uid',                                                             # 用户ID
        'balance_usdt',                                                    # USDT余额E2
        'balance_btc',                                                     # 最新BTC余额 单位E8
        'balance_eth',                                                     # 最新ETH余额 单位E8
        'create_time',                                                     # 创建时间
        'update_time',                                                     # 更新时间
    ]