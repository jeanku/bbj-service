#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class HedgeOrderModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'hedge_order'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                               # 自增ID
        'open_order_id',                                                    # 开仓合作平台orderId
        'type',                                                             # 下单类型1:限价单 2:市价单
        'bs_flag',                                                          # 1:买跌2:买涨
        'leverage',                                                         # 杠杆2,3,5,10,20,33,50,100
        'open_amount',                                                      # 对冲合约金额
        'close_amount',                                                     # 已平合约金额
        'pl_e2',                                                            # 盈亏金额
        'open_time',                                                        # 开仓时间
        'create_time',                                                      # 
        'update_time',                                                      # 
    ]