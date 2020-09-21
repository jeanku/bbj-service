#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class FundUserModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'fund_user'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                      # 自增ID
        'uid',                                                                     # 用户ID
        'balance_e2',                                                              # 最新余额，单位：分
        'balance_usdt',                                                            # 钱包USDT账户
        'futures_usdt_balance',                                                    # 永续合约账户可用金额
        'futures_usdt_freeze',                                                     # 永续合约冻结金额
        'futures_balance_usdt',                                                    # //合约冻结金额
        'futures_balance_e2',                                                      # 合约账户
        'balance_freeze_e2',                                                       # 冻结余额，单位：分
        'balance_coupon_e2',                                                       # 券盈利金额，单位：分
        'coupon_count',                                                            # 
        'balance_btc',                                                             # 最新BTC余额 单位e10-8
        'balance_eth',                                                             # 最新ETH余额 单位e10-8
        'balance_eos',                                                             # 最新eos余额 单位e10-8
        'balance_dai',                                                             # 最新DAI余额 单位e10-8
        'balance_key',                                                             # 最新key余额 单位e10-8
        'balance_trx',                                                             # 最新trx余额 单位e10-8
        'balance_bch',                                                             # 最新bch余额 单位e10-8
        'balance_pax',                                                             # 最新pax余额 单位e10-8
        'creadits_e4',                                                             # eos兑换积分1:20,单位e10-4
        'total_pl',                                                                # 累计盈亏，单位：分
        'create_time',                                                             # 创建时间
        'update_time',                                                             # 更新时间
        'grants_e2',                                                               # 赠金
        'back_commition_e2',                                                       # 返佣
        'balance_usdc',                                                            # 最新usdc余额
        'ex_balance_e2',                                                           # 体验金余额, e2
        'ex_valid_time',                                                           # 体验金有效时间
    ]