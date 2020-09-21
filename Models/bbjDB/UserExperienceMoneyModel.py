#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class UserExperienceMoneyModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'user_experience_money'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                              # 自增ID
        'uid',                                                             # 用户ID
        'orderusdt_e2',                                                    # 赠送金额(USDT)
        'currency_id',                                                     # 币种
        'amount_e8',                                                       # 币数量
    ]