#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class LiveTypeModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'live_type'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 
        'type',                                                           # 直播类型
        'type_color',                                                     # 类型色值
        'name_color',                                                     # 标题色值
        'status',                                                         # 状态 1:正常 0:删除
        'rank',                                                           # 排序
        'create_time',                                                    # 创建时间
        'update_time',                                                    # 更新时间
    ]