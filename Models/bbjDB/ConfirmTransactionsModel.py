#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class ConfirmTransactionsModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'confirm_transactions'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                               # 
        'uid',                                                              # 用户id
        'is_extract',                                                       # 是否提取到账户，0:没有，1:已提取
        'contract_id',                                                      # 币种
        'tx_hash',                                                          # 交易hash
        'from_address',                                                     # 发送地址
        'to_address',                                                       # 接收地址
        'amount_e8',                                                        # 交易额
        'block_number',                                                     # 区块高度
        'tx_fee_e8',                                                        # 手续费单位BTC
        'token_type',                                                       # 代币类型，1:omni,2:erc20;3:EOS
        'is_transfered',                                                    # 是否被转走到中心地址,0:没有,确认中 1:到账；3:eos转移到提币账户;4:无效充值
        'out_txhash',                                                       # 转账hash
        'create_time',                                                      # 充值时间
    ]