#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class MarketPrice202009Model(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'market_price_202009'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'm_id',                                                             # 自增ID
        'm_contract_id',                                                    # 币类型：btc
        'm_newprice_e4',                                                    # 价格
        'm_seq',                                                            # 时间
        'm_state',                                                          # 
        'm_update_time',                                                    # 更新时间
    ]