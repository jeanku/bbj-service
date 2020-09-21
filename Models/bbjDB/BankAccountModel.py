#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class BankAccountModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'bank_account'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 自增ID
        'uid',                                                            # 用户ID
        'pay_type',                                                       # 支付类型 1支付宝 2银行卡 ...
        'qr_img',                                                         # 支付二维码图片路径
        'name',                                                           # 姓名
        'bank',                                                           # 银行名称
        'account',                                                        # 收款账号
        'create_time',                                                    # 创建时间
        'update_time',                                                    # 更新时间
        'status',                                                         # 状态1：正常0：删除
    ]