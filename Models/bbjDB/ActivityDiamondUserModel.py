#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class ActivityDiamondUserModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'activity_diamond_user'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # ID
        'uid',                                                            # uid
        'start_time',                                                     # 开始时间
        'end_time',                                                       # 结束时间
        'create_time',                                                    # 创建时间
        'update_time',                                                    # 更新时间
    ]