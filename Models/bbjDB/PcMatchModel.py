#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PcMatchModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'pc_match'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                         # 主键
        'match_time',                                                                 # 成交时间
        'contract_id',                                                                # 交易对ID、合约号
        'exec_id',                                                                    # 成交编号
        'bid_uid',                                                                    # 买方账号ID
        'ask_uid',                                                                    # 卖方账号ID
        'bid_order_id',                                                               # 买方委托号
        'ask_order_id',                                                               # 卖方委托号
        'match_price',                                                                # 成交价
        'match_qty',                                                                  # 成交数量
        'match_amt',                                                                  # 成交金额
        'bid_fee',                                                                    # 买方手续费
        'ask_fee',                                                                    # 卖方手续费
        'bid_open_price',                                                             # 成交时的建仓均价
        'ask_open_price',                                                             # 成交时的建仓均价
        'bid_contract_qty',                                                           # 成交时的建仓量
        'ask_contract_qty',                                                           # 成交时的建仓量
        'bid_close_price',                                                            # 成交后的平仓均价
        'ask_close_price',                                                            # 成交后的平仓均价
        'bid_closed_qty',                                                             # 成交后的平仓量
        'ask_closed_qty',                                                             # 成交后的平仓量
        'marked_price',                                                               # 成交时的标记价格
        'maintenance_margin_rate',                                                    # 成交时的维持保证金率
        'is_taker',                                                                   # Taker方向
        'update_time',                                                                # 最近更新时间
        'create_time',                                                                # 
    ]