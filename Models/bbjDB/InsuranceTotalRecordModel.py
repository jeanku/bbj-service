#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class InsuranceTotalRecordModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'insurance_total_record'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                 # 
        'date',                                                               # 日期
        'total_amount_e2',                                                    # 总金额
        'used_amount_e2',                                                     # 已使用金额
        'create_time',                                                        # 
    ]