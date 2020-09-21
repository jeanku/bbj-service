#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class OtcOrdersModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'otc_orders'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                              # 
        'order_id',                                                        # 下单id
        'platorder_id',                                                    # 平台订单id
        'uid',                                                             # 用户di
        'price',                                                           # 成交价
        'qty',                                                             # 成交量
        'fee',                                                             # 费用
        'side',                                                            # 方向
        'order_type',                                                      # 订单成交类型；市价，限价。。。
        'timestamp',                                                       # 时间
        'platform',                                                        # 0:币安;
        'app_id',                                                          # 平台订单id
        'profit_e2',                                                       # 盈亏
        'balance_e8',                                                      # 余额
    ]