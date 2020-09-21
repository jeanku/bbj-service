#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class HedgeOrderFlowModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'hedge_order_flow'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                # 自增ID
        'uid',                                                               # 用户UID
        'trade_order_id',                                                    # 建仓ID
        'open_order_id',                                                     # 开仓合作平台orderId
        'lever_amount',                                                      # 合约建仓金额
        'bs_flag',                                                           # 标志：1买跌 2买涨
        'open_time',                                                         # 对冲时间
        'close_hedge',                                                       # 0:开仓 1:平仓
        'close_time',                                                        # 对冲平仓时间
        'close_order_id',                                                    # 对冲平仓id
        'create_time',                                                       # 
        'update_time',                                                       # 
    ]