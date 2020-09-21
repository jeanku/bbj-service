#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class RiskLimitModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'risk_limit'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                         # 自增id
        'contract_amount',                                                            # 合约价值范围
        'maintenance_margin_rate',                                                    # 维持保证金率
        'min_initial_margin_rate',                                                    # 最低初始保证金率
        'max_lever',                                                                  # 最大杠杆
        'level',                                                                      # 层级
        'create_time',                                                                # 创建时间
        'update_time',                                                                # 更新时间
    ]