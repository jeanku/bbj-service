#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PcCashFlowModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'pc_cash_flow'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                      # 
        'uid',                                                                     # 用户ID
        'order_id',                                                                # 委托订单
        'user_order_id',                                                           # 持仓单ID
        'category',                                                                # 金额类型
        'balance',                                                                 # 金额。从用户扣钱为正，向用户付钱为负。
        'futures_usdt_balance',                                                    # 操作前永续合约账户余额
        'futures_usdt_freeze',                                                     # 操作前永续合约账户冻结金额
        'amount',                                                                  # 保证金金额
        'open_fee',                                                                # 开仓手续费
        'close_fee',                                                               # 平仓手续费
        'profit',                                                                  # 收益
        'comment',                                                                 # 备注
        'create_time',                                                             # 创建时间（毫秒）
    ]