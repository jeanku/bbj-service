#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class BannerModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'banner'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                               # 
        'title',                                                            # 标题
        'url',                                                              # 七牛地址
        'redirect_url',                                                     # 跳转地址
        'status',                                                           # 状态 0下架 1上架
        'for_new_user',                                                     # 
        'create_time',                                                      # 创建时间
        'update_time',                                                      # 更新时间
        'platform_type',                                                    # 展示平台|0=>手机端,1=>pc端
        'language_type',                                                    # 语言类型，默认中文
    ]