#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class AgentSuperApplyModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'agent_super_apply'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                             # 
        'uid',                                                            # UID
        'name',                                                           # 姓名
        'country',                                                        # 居住国家
        'email',                                                          # 邮箱
        'propaganda',                                                     # 宣传账号、链接
        'plan',                                                           # 宣传计划
        'media',                                                          # 社交媒体
        'db',                                                             # 指派审核人
        'check',                                                          # 审核状态：0:未审核 1:通过 2:拒绝
        'create_time',                                                    # 创建时间
        'update_time',                                                    # 更新时间
    ]