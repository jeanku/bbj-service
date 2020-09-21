#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class HedgeDealModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'hedge_deal'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                               # 自增ID
        'open_order_id',                                                    # 开仓合作平台orderId
        'type',                                                             # 下单类型1:限价单 2:市价单
        'side',                                                             # 仓位方向Buy:多仓 Sell:空仓
        'leverage',                                                         # 杠杆2,3,5,10,20,33,50,100
        'price_e4',                                                         # 下单价格,市价单可以为空
        'open_fee_e2',                                                      # 建仓手续费
        'pl_e2',                                                            # 盈亏金额
        'open_time',                                                        # 开仓时间
        'exec_qty',                                                         # 成交量
        'exec_id',                                                          # 执行id
    ]