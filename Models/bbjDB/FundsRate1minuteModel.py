#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class FundsRate1minuteModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'funds_rate_1minute'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 
        'date_time',                                                      # 当前时间
        'currency_id',                                                    # 币种
        'rate_e6',                                                        # 资金费率 + 扣除多方；-扣除空方
        'pre_rate_e6',                                                    # 预测的资金费率
    ]