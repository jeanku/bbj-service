#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class AgentRebateLogModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'agent_rebate_log'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                       # 自增ID
        'uid',                                                                      # 用户ID
        'system_rebate_rate_e2',                                                    # 赠送金额(USDT)
        'create_time',                                                              # 创建时间
    ]