#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class ChatRoomNoticeModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'chat_room_notice'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                # 自增ID
        'title',                                                             # 标题
        'content',                                                           # 内容
        'status',                                                            # 状态：0：下架，1：启用
        'type',                                                              # 1普通消息
        'link_url',                                                          # 链接
        'link_url_desc',                                                     # 链接描述
        'link_url1',                                                         # 链接1
        'link_url1_desc',                                                    # 链接描述1
        'create_time',                                                       # 创建时间
        'update_time',                                                       # 更新时间
    ]