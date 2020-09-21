#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class MarketPrice30minkModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'market_price_30mink'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 自增ID
        'trade_date',                                                     # 交易日
        'data_time',                                                      # 交易时刻
        'contract_id',                                                    # 行情品种ID
        'openprice',                                                      # 开盘价
        'highprice',                                                      # 最高价
        'lowprice',                                                       # 最低价
        'closeprice',                                                     # 收盘价
        'volume',                                                         # 成交量
        'amount',                                                         # 成交额
        'totalvolume',                                                    # 总成交量
        'totalamount',                                                    # 总成交额
        'ma5_price',                                                      # 均线
        'ma10_price',                                                     # 均线
        'ma30_price',                                                     # 均线
    ]