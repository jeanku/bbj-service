#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class HedgeChainextModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'hedge_chainext'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                         # 
        'chainext_btc_amount_e8',                                                     # 做市商btc
        'chainext_usdt_amount_e8',                                                    # 做市商usdt
        'pre_btc_amount_e8',                                                          # 对冲前btc
        'pre_usdt_amount_e8',                                                         # 
        'hedge_amount_e8',                                                            # 对冲量
        'side',                                                                       # 方向
        'create_time',                                                                # 
        'state',                                                                      # 状态，0失败，1成功
        'after_btc_amount_e8',                                                        # 对冲后
        'after_usdt_amount_e8',                                                       # 
        'total_btc_e8',                                                               # 总量btc
        'total_usdt_e8',                                                              # 总量usdt
        'btc_profit_e8',                                                              # btc盈亏
        'usdt_profit_e8',                                                             # usdt盈亏
        'price_e4',                                                                   # btc价格
    ]