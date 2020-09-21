#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class FundsBillModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'funds_bill'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                 # 
        'uid',                                                                # 用户di
        'order_id',                                                           # 订单id
        'bs_flag',                                                            # 方向
        'balance_e2',                                                         # 用户余额
        'capital_cost_e2',                                                    # 资金费用 已经乘以100
        'force_price_e2',                                                     # 强平价
        'rate_e6',                                                            # 
        'date_time',                                                          # 
    ]