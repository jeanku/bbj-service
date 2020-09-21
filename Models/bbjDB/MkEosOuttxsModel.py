#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class MkEosOuttxsModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'mk_eos_outtxs'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                              # 
        'uid',                                                             # 
        'order_id',                                                        # 提币请求id
        'txid',                                                            # 提币交易id
        'from_address',                                                    # 
        'to_address',                                                      # 
        'amount_e4',                                                       # 提积分额度
        'create_time',                                                     # 提币时间
        'status',                                                          # 0:失败，1:成功;2:确认中
    ]