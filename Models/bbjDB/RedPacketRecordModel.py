#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class RedPacketRecordModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'red_packet_record'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 
        'uid',                                                            # 用户id
        'rid',                                                            # 红包id
        'amount',                                                         # 金额单位聪
        'create_time',                                                    # 
        'currency_id',                                                    # 
        'type',                                                           # 1:app内红包 2：口令红包
        'username',                                                       # 发红包人的名字
        'is_max',                                                         # 是否手气最佳：0:否 1：是
    ]