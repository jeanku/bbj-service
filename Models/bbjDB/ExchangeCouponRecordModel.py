#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class ExchangeCouponRecordModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'exchange_coupon_record'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                  # 
        'uid',                                                                 # 
        'coupon_amount_e2',                                                    # 
        'coupon_nums',                                                         # 
        'create_time',                                                         # 
        'update_time',                                                         # 
        'btc_e8',                                                              # 
        'status',                                                              # 1:正常 0：删除
    ]