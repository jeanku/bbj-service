#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PayaddrlistUserModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'payaddrlist_user'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 自增ID
        'uid',                                                            # UID
        'inaddr_type',                                                    # 类型：1omni,2erc20,3:EOS;
        'currency_id',                                                    # 币种
        'inaddr',                                                         # 地址
        'create_time',                                                    # 创建时间
        'balance_e8',                                                     # 
        'state',                                                          # 0禁用1启用
        'update_time',                                                    # 更新时间
        'account',                                                        # 账户名
        'app_id',                                                         # 
    ]