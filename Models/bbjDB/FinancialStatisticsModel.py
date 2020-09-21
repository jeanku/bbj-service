#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class FinancialStatisticsModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'financial_statistics'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                              # 
        'uid',                                                             # 用户id
        'day_interest',                                                    # 当日收益
        'balance_usdt',                                                    # 当日余额
        'day',                                                             # 统计日期
        'create_time',                                                     # 
        'update_time',                                                     # 
    ]