#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PcClosedOrderModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'pc_closed_order'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                            # 
        'uid',                                                           # 
        'order_id',                                                      # 持仓单id
        'amount',                                                        # 成交额
        'closed_qty',                                                    # 平仓量
        'close_time',                                                    # 成交时间
        'close_type',                                                    # 平仓类型
    ]