#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class RedPacketNormalModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'red_packet_normal'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                # 
        'uid',                                                               # 用户id
        'rid',                                                               # 红包id
        'amount',                                                            # 总金额，btc为e8，usdt为e2
        'nums',                                                              # 总数量
        'create_time',                                                       # 创建时间
        'update_time',                                                       # 修改时间
        'end_time',                                                          # 过期时间
        'currency_id',                                                       # 币种
        'max_uid',                                                           # 手气最佳uid
        'type',                                                              # 2:口令红包 3：普通红包
        'channel',                                                           # 渠道
        'red_packet_key',                                                    # 口令
        'state',                                                             # 1:生效 -1无效
        'addition',                                                          # 备注
        'price',                                                             # 当前价格
        'is_end',                                                            # 是否抢光 ：0：否 1：是
        'content',                                                           # 红包说明
    ]