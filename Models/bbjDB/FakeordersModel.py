#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class FakeordersModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'fakeorders'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                # 
        'timestamp',                                                         # 
        'open_time',                                                         # 
        'open_price_e4',                                                     # 
        'now_price_e4',                                                      # 现价
        'dvalue',                                                            # 涨跌金额差e2
        'dprice',                                                            # 收开差价e4
        'fake_dprice_e4',                                                    # 造价差
        'fake_price_e4',                                                     # 造价
        'probility',                                                         # 概率是否造价
        'dprice_fake',                                                       # 差价上是否造假
        'dvalue_fake',                                                       # 金额上是否造假
        'total_up_e2',                                                       # 买涨总额
        'total_down_e2',                                                     # 买跌总额
        'nums',                                                              # 数量
    ]