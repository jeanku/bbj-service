#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class GuessOrderModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'guess_order'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                   # 自增ID
        'uid',                                                                  # 用户ID
        'open_amount_e2',                                                       # 建仓金额(本金) 单位:分
        'pl_usdt',                                                              # 盈亏金额换算成USDT
        'open_amount_usdt',                                                     # //换算成USDT
        'contract_id',                                                          # 行情价格ID
        'currency_id',                                                          # 币种
        'bs_flag',                                                              # 标志：1看跌 2看涨
        'period',                                                               # 周期；1，5，10，30，60
        'yield_rate_e2',                                                        # 收益率
        'open_price_e4',                                                        # 建仓价
        'open_new_price_id',                                                    # 建仓时的行情逐笔ID
        'open_time',                                                            # 建仓时间
        'close_type',                                                           # 平仓类型 3建仓 4预测成功5预测失败6无效 
        'close_price_e4',                                                       # 平仓价
        'close_time',                                                           # 平仓时间
        'pl_e2',                                                                # 盈亏金额
        'balance_e2',                                                           # 建仓前余额
        'channel',                                                              # 1.平台 2.mykey
        'cost_token',                                                           # 1:usdt；2：eos
        'is_made',                                                              # 是否被微创 1是 0 否
    ]