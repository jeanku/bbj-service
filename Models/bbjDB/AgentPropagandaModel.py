#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class AgentPropagandaModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'agent_propaganda'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                 # 
        'uid',                                                                # UID
        'friend_rabateE4',                                                    # 好友反现比例
        'agent_rebateE4',                                                     # 代理反现比例
        'cycle',                                                              # 反现周期:0:1周；1:1个月；2:3个月；4:半年
        'invite_code',                                                        # 邀请码
        'valid',                                                              # 1:有效；2:无效
        'remark',                                                             # 备注
        'location',                                                           # 推广跳转的地点
        'lang',                                                               # 语言
        'sys',                                                                # 是否系统自动生成。1：是；2：否
        'create_time',                                                        # 创建时间
        'update_time',                                                        # 更新时间
    ]