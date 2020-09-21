#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class CouponModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'coupon'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                   # 自增ID
        'title',                                                                # 券名称
        'coupon_num',                                                           # 券总量
        'coupon_amount_e2',                                                     # BTC数量 单位:0.01BTC*100
        'lever',                                                                # 杠杆
        'remark',                                                               # 备注
        'create_time',                                                          # 创建时间
        'update_time',                                                          # 更新时间
        'min_spratio',                                                          # 最小止盈比例/100
        'max_spratio',                                                          # 最大止盈比例/100
        'max_force_spratio',                                                    # 最大强制止盈比例/100
        'state',                                                                # 状态：1启用，0关闭
    ]