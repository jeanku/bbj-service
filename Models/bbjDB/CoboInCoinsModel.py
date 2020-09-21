#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class CoboInCoinsModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'cobo_in_coins'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                # 
        'uid',                                                               # 
        'order_id',                                                          # 
        'cobo_id',                                                           # cobo交易id
        'coin',                                                              # 币种名称缩写
        'txid',                                                              # 链上交易id
        'source_address',                                                    # 来源地址
        'amount',                                                            # 数量
        'abs_cobo_fee',                                                      # cobo手续费
        'created_time',                                                      # 开收时间
        'last_time',                                                         # 结束时间
        'fee_coin',                                                          # 交易费币种
        'fee_amount',                                                        # 链上费
        'fee_decimal',                                                       # 对应币种的decimal
        'status',                                                            # j交易状态
        'balance_e8',                                                        # 对应币种下单后余额
    ]