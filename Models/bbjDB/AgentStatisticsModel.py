#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class AgentStatisticsModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'agent_statistics'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                  # 
        'uid',                                                                 # 合伙人uid
        'order_uid',                                                           # 订单产生uid
        'day',                                                                 # 订单日：20190828
        'instrument_id',                                                       # t_d_trade表的标的InstrumentId代码字段
        'product_id',                                                          # t_d_trade表的标的ProductID代码字段
        'amount_currency',                                                     # 合约价值币种
        'rebate_currency',                                                     # 反佣币种
        'level',                                                               # 同agent_record表的level字段
        'total',                                                               # 超级合伙人总金额（按币种）（所有层级下线）
        'rebate',                                                              # 超级合伙人总收益（按币种）（所有层级下线）
        'total_usdt_rate',                                                     # 金额币种到USDT的汇率
        'total_btc_rate',                                                      # 金额币种到BTC的汇率
        'rebate_usdt_rate',                                                    # 反佣币种到USDT的汇率
        'rebate_btc_rate',                                                     # 反佣币种到BTC的汇率
        'create_time',                                                         # 创建时间
        'update_time',                                                         # 更新时间
    ]