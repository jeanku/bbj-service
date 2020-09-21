#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class AgentUserTradeStatisticsModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'agent_user_trade_statistics'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                  # 
        'uid',                                                                 # 交易者UID
        'day',                                                                 # YYYYMMDD格式日期
        'instrument_id',                                                       # t_d_trade表的InstrumentID字段
        'product_id',                                                          # t_d_trade表的ProductID字段
        'amount_currency',                                                     # 成交币种
        'rebate_currency',                                                     # 反佣的币种
        'taker',                                                               # taker交易量
        'maker',                                                               # maker交易量
        'taker_fee',                                                           # taker手续费
        'maker_fee',                                                           # maker手续费
        'rebate',                                                              # 反佣
        'total_usdt_rate',                                                     # 金额币种到USDT的汇率
        'total_btc_rate',                                                      # 金额币种到BTC的汇率
        'rebate_usdt_rate',                                                    # 反佣币种到BTC的汇率
        'rebate_btc_rate',                                                     # 反佣币种到BTC的汇率
        'create_time',                                                         # 创建时间
        'update_time',                                                         # 更新时间
    ]