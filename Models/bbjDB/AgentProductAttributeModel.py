#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class AgentProductAttributeModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'agent_product_attribute'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                               # 
        'instrument_id',                                                                    # t_d_trade表的标的InstrumentID代码字段
        'product_id',                                                                       # t_d_trade表的标的ProductID代码字段
        'name',                                                                             # 显示的产品名
        'currency',                                                                         # 交易币种
        'usdt_exchange_rate_key',                                                           # 交易币种在otc_exchange中转换成UDST的KEY。如果为""，则表示1
        'rebate_currency',                                                                  # 反佣币种
        'rebate_usdt_exchange_rate_key',                                                    # 反佣交易币种在otc_exchange中转换成UDST的KEY。""表示1
        'create_time',                                                                      # 创建时间
        'update_time',                                                                      # 最后更新时间
    ]