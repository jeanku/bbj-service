#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PushModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'push'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 
        'title',                                                          # 标题
        'content',                                                        # 内容
        'left_url',                                                       # 左链接
        'right_url',                                                      # 右链接
        'type',                                                           # 类型
        'status',                                                         # 状态 0下架 1上架
        'create_time',                                                    # 创建时间
        'update_time',                                                    # 更新时间
    ]