#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class RedPacketModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'red_packet'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 
        'amount_e4',                                                      # 红包金额单位usdt
        'uid',                                                            # 用户id
        'order_id',                                                       # 订单id
        'nums',                                                           # 红包数量
        'create_time',                                                    # 
        'end_time',                                                       # 
        'rid',                                                            # 红包id
        'price',                                                          # 当前价格
        'red_type',                                                       # 类型
        'types',                                                          # 1订单红包 2聊天室红包
        'is_sp',                                                          # 手动盈亏0：默认老的 1:亏 损；2：盈利
        'max_uid',                                                        # 此次最佳
    ]