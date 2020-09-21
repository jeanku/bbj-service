#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class AppendBailRecordModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'append_bail_record'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                  # 
        'order_id',                                                            # 
        'append_amount_e2',                                                    # 
        'create_time',                                                         # 
        'type',                                                                # 1:自动 2：手动
        'flag',                                                                # 1:增 2：减
        'open_amt_e2',                                                         # 追加前金额
        'lever_e2',                                                            # 追加前杠杆
        'balance_e2',                                                          # 追加前余额
        'ex_balance_e2',                                                       # 追加前体验金余额
    ]