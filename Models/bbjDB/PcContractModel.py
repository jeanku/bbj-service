#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PcContractModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'pc_contract'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'contract_id',                                                              # 
        'symbol',                                                                   # 交易对名称
        'lot_size',                                                                 # 最小交易量单位
        'taker_fee_ratio',                                                          # Taker手续费率
        'maker_fee_ratio',                                                          # Maker手续费率
        'display_precision',                                                        # 显示精度
        'price_precision',                                                          # 价格精度
        'market_max_level',                                                         # 市价成交最大档位
        'max_num_orders',                                                           # 最大挂单笔数
        'commodity_id',                                                             # 商品币种ID
        'currency_id',                                                              # 货币币种ID
        'contract_status',                                                          # 交易对状态：1上架 2下架
        'list_time',                                                                # 上市时间，微秒时间戳
        'rank',                                                                     # 排序
        'contract_type_support',                                                    # 支持仓位模式 1.全仓 2逐仓 3.全仓，逐仓
        'limit_type',                                                               # 约束类型 1档位约束
        'max_lever_rule',                                                           # 满挡处理规则 1.撤单 2.重新挂单
        'status',                                                                   # 状态 1有效 0删除
        'create_time',                                                              # 创建时间
        'update_time',                                                              # 修改时间
    ]