#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PcCurrencyModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'pc_currency'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'currency_id',                                                          # 币种
        'symbol',                                                               # 币种名称
        'name_cn',                                                              # 币种中文名
        'symbol_desc',                                                          # 币种简介
        'display_precision',                                                    # 页面显示位数
        'prefix_url',                                                           # 币种浏览器地址
        'inter_rate',                                                           # 币种贷款利率
        'enabled',                                                              # 币状态：0不启用,1启用,2删除
        'logo',                                                                 # 
        'rank',                                                                 # 排序
    ]