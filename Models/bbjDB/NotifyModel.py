#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class NotifyModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'notify'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 自增ID
        'uid',                                                            # uid
        'title',                                                          # 标题
        'content',                                                        # 内容
        'route_json',                                                     # 路由:'reg':注册  'coupon'：送券
        'create_time',                                                    # 创建时间
        'update_time',                                                    # 更新时间
        'state',                                                          # 状态：0删除，1未读 2已读
        'type',                                                           # 类型 ：reg：注册 coupon：发券 normal：普通
    ]