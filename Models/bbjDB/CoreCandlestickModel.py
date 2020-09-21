#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class CoreCandlestickModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'core_candlestick'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'appl_id',                                                        # 应用标识
        'contract_id',                                                    # 交易对ID
        'range',                                                          # K线类型
        'time',                                                           # 行情时间
        'open_price',                                                     # 开盘价
        'close_price',                                                    # 收盘价
        'high_price',                                                     # 最高价
        'low_price',                                                      # 最低价
        'volume',                                                         # 成交量
        'turnover',                                                       # 
    ]