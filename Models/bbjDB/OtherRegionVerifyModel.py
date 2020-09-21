#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class OtherRegionVerifyModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'other_region_verify'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 
        'uid',                                                            # 用户id
        'region',                                                         # 地区
        'name',                                                           # 姓名
        'credentials',                                                    # 证件类型
        'card_no',                                                        # 证件号码
        'create_time',                                                    # 创建时间
        'update_time',                                                    # 更新时间
    ]