#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class Erc20PendTxModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'erc20_pend_tx'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                               # 
        'tx_hash',                                                          # 充币hash
        'block_hash',                                                       # 区块hash
        'block_num',                                                        # 区块高度16进制
        'confirm_count',                                                    # 确认次数
        'tx_index',                                                         # 交易index 16进制
        'from_address',                                                     # 充币地址
        'to_address',                                                       # 接收地址
        'amount',                                                           # 金额，16进制;decimal:6
    ]