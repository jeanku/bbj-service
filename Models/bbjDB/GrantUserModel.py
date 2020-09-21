#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class GrantUserModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'grant_user'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                 # 
        'uid',                                                                # 用户id
        'grant_amount_e2',                                                    # 面额 单位：0.01个USDT*100
        'create_time',                                                        # 创建时间
        'remark',                                                             # 备注
        'phone',                                                              # 邀请用户手机号
        'src',                                                                # 1注册 2邀请 3下单 4后台赠送,5BTC券转化,6首冲成功送赠金,7竞猜失败赠送 8巴比特活动送
        'update_time',                                                        # 更新时间
        'order_id',                                                           # 订单id
        'oid',                                                                # 关联id
    ]