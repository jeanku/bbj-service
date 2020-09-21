#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class RedPacketUserModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'red_packet_user'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                     # 
        'uid',                                                                    # 
        'left_nums',                                                              # 剩余抢红包次数
        'order_complete_nums',                                                    # 订单完成次数
        'sp_nums',                                                                # 100%止盈次数
        'sl_nums',                                                                # 100%止损次数
        'inmoney_nums',                                                           # 充值次数
        'share_nums',                                                             # 分享次数
        'invite_nums',                                                            # 邀请次数
        'verified_nums',                                                          # 实名认证次数
        'create_time',                                                            # 
        'update_time',                                                            # 
    ]