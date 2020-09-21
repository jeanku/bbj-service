#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class LiveroomModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'liveroom'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 
        'roomid',                                                         # 房间id
        'cid',                                                            # 创建人id
        'name',                                                           # 名称
        'start_time',                                                     # 直播开始时间
        'announce',                                                       # 预告
        'tid',                                                            # 类型id
        'status',                                                         # 状态 1已创建 2:开始预告 3:停止预告 4.开始直播 5.停止直播 -1.删除
        'link_url',                                                       # 链接
        'most_online',                                                    # 最高在线人数
        'create_time',                                                    # 创建时间
        'update_time',                                                    # 更新时间
    ]