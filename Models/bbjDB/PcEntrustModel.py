#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PcEntrustModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'pc_entrust'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 
        'uid',                                                            # 用户ID
        'order_id',                                                       # 订单号
        'data',                                                           # 委托数据
        'type',                                                           # 1:反向 2:正向 3:现货
        'status',                                                         # 委托状态  1.待执行委托 2已执行委托 3已撤销 4失效 5已触发
        'create_time',                                                    # 委托时间
        'update_time',                                                    # 更新时间
    ]