#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class OutTransactionsModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'out_transactions'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                              # 
        'out_txhash',                                                      # 转账hash
        'tx_fee_e8',                                                       # 手续费,单位BTC
        'from_address',                                                    # 发送地址
        'to_address',                                                      # 接收地址
        'amount_e8',                                                       # 转账金额
        'block_number',                                                    # 
        'token_type',                                                      # 1:omni;2:erc20;3:EOS
    ]