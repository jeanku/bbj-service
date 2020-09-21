#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class AgentRecordModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'agent_record'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                      # 
        'partner_uid',                                                             # 合伙人uid
        'trade_id',                                                                # t_d_trade表中的TradeID（成交代码）字段
        'direction',                                                               # t_d_trade表中的Direction（1.买2.卖）字段
        'order_id',                                                                # 订单id
        'order_uid',                                                               # 订单对应的uid
        'contract_amount',                                                         # 合约价值
        'fee',                                                                     # 手续费
        'grants_fee',                                                              # 赠金抵扣
        'phone',                                                                   # 
        'name',                                                                    # 订单创建人
        'rebate',                                                                  # 返佣金额
        'level',                                                                   # 提成层级。如果是从子代理线上来的，用正数层级；如果是从好友线上来的，用负数层级。如果发生时partner_uid是普通合伙人，需要在原level基础上加减64
        'state',                                                                   # 1：有效 0：删除
        'is_send',                                                                 # 是否发送返佣 1已发送 0未发送 -1已拒绝
        'send_time',                                                               # 审核时间
        'trade_time',                                                              # t_d_trade表的TradeTime字段
        'day',                                                                     # 订单日：20190828
        'month',                                                                   # 订单月：201908
        'child_uid',                                                               # 直接邀请人
        'instrument_id',                                                           # t_d_trade表的InstrumentID字段
        'product_id',                                                              # t_d_trade表的ProductID字段
        'amount_currency',                                                         # 合约价值币种
        'rebate_currency',                                                         # 反佣币种
        'exchange_rate',                                                           # 转化成USDT的汇率
        'btc_exchange_rate',                                                       # USDT转化成BTC的汇率
        'rebate_exchange_rate',                                                    # 反佣转化成USDT的汇率
        'exchange_rate_time',                                                      # 汇率计算的时间点（毫秒）
        'create_time',                                                             # 
        'update_time',                                                             # 最后修改时间
    ]