#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class ExRecordModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'ex_record'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                               # 
        'amount_e2',                                                        # 发送金额
        'type',                                                             # 1:新手 2：进阶 3:后台发送
        'tid',                                                              # 
        'uid',                                                              # 
        'ex_balance_e2',                                                    # 发送前体验金余额
        'create_time',                                                      # 
        'update_time',                                                      # 
    ]