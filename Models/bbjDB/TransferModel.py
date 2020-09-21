#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class TransferModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'transfer'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 自增ID
        'balance_e8',                                                     # 划转前余额
        'from_id',                                                        # 来源ID：1主账户2合约账户99其它账户
        'to_id',                                                          # 目标ID：1主账户2合约账户99其它账户
        'currency_id',                                                    # 币种
        'amount_e8',                                                      # 币数量
        'uid',                                                            # 用户ID
        'state',                                                          # 状态：0划转提交1划转成功99划转失败
        'app_id',                                                         # 合作平台ID：1BBJ
        'update_time',                                                    # 更新时间
        'create_time',                                                    # 创建时间
        'flow_id',                                                        # 三方平台订单ID
        'type',                                                           # 类型
    ]