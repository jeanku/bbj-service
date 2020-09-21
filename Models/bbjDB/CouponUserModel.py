#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class CouponUserModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'coupon_user'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                  # 自增ID
        'uid',                                                                 # 用户ID
        'c_id',                                                                # 券ID
        'c_title',                                                             # 券名称
        'coupon_amount_e2',                                                    # 券面额(BTC数量) 单位：0.01个BTC*100
        'lever',                                                               # 杠杆
        'start_time',                                                          # 有效期开始时间
        'end_time',                                                            # 有效期结束时间
        'state',                                                               # 状态 1有效 2已使用 -1过期
        'create_time',                                                         # 创建时间
        'remark',                                                              # 备注
        'update_time',                                                         # 更新时间
        'type',                                                                # 1:新人券 2：亏损送券 3：手动送， 4：邀请送券
    ]