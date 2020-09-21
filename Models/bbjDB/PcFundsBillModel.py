#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PcFundsBillModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'pc_funds_bill'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                               # 
        'uid',                                                              # 用户di
        'contract_type',                                                    # 模式类型
        'order_id',                                                         # 持仓订单id
        'bs_flag',                                                          # 标志：1看跌 2看涨
        'balance',                                                          # 用户余额
        'capital_cost',                                                     # 资金费用
        'mark_price',                                                       # 当前标记价
        'force_price',                                                      # 强平价
        'fund_rate',                                                        # 资金费率
        'date_time',                                                        # 
    ]