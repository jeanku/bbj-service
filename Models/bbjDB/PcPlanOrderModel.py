#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PcPlanOrderModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'pc_plan_order'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'order_id',                                                         # 订单id
        'uid',                                                              # 用户ID
        'contract_id',                                                      # 交易对
        'side',                                                             # 方向 1.开仓 2.平仓
        'amount',                                                           # 保证金
        'lever',                                                            # 杠杆
        'bs_flag',                                                          # 标志 1.看跌 2.看涨
        'price',                                                            # 委托价
        'quantity',                                                         # 委托量
        'order_type',                                                       # 委托类型 1.市价 2.限价
        'trigger_price',                                                    # 触发价
        'dir',                                                              # 方向 1.≥ 2.≤
        'order_status',                                                     # 委托状态  1.待创建委托 2已创建委托 3已撤销 4失效 5已触发
        'pc_order_id',                                                      # 委托单ID
        'user_order_id',                                                    # 持仓单id
        'trade_time',                                                       # 委托时间
        'create_time',                                                      # 委托时间
        'update_time',                                                      # 更新时间
    ]