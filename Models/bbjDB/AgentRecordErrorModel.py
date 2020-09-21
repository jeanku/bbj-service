#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class AgentRecordErrorModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'agent_record_error'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'trade_id',                                                        # 成交代码
        'direction',                                                       # 1.买2.卖
        'order_sys_id',                                                    # 报单系统唯一代码
        'error',                                                           # 报错
        'create_time',                                                     # 创建时间
        'update_time',                                                     # 更新时间
    ]