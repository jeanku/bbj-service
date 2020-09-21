#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class AgentRebateModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'agent_rebate'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 
        'uid',                                                            # 合伙人ID
        'date',                                                           # YYYYMMDD格式日期
        'type',                                                           # 分类：1.反向合约佣金
        'currency',                                                       # 币种
        'money',                                                          # 金额
        'usdt_ratio',                                                     # 换算成USDT的汇率.money×usdt_ratio=usdt金额
        'btc_ratio',                                                      # 换算成BTC的汇率.money×btc_ratio=btc金额
        'remark',                                                         # 备注
        'create_time',                                                    # 创建时间
        'update_time',                                                    # 更新时间
    ]