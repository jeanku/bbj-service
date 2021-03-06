#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class FinancialInterestModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'financial_interest'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                               # 自增ID
        'uid',                                                              # 用户ID
        'balance_usdt',                                                     # 清算前钱包账户余额 单位e10-8
        'balance_total',                                                    # 清算前总账户余额
        'rate',                                                             # 年化利率 单位e10-4
        'rate_second',                                                      # 秒化利率 单位e10-10
        'interest',                                                         # 利息
        'day',                                                              # 创建日期
        'create_time',                                                      # 创建时间
        'update_time',                                                      # 更新时间
    ]