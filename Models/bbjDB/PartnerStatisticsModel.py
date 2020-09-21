#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PartnerStatisticsModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'partner_statistics'  # 表名

    __create_time__ = None  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                  # 
        'uid',                                                                 # 合伙人uid
        'day_total_e2',                                                        # 当日金额
        'day_rebate_e2',                                                       # 当日收益
        'month_total_e2',                                                      # 当月金额
        'month_rebate_e2',                                                     # 当月收益
        'first_rebate_e2',                                                     # 一级返佣
        'second_rebate_e2',                                                    # 二级返佣
        'third_rebate_e2',                                                     # 
        'rebate_e2',                                                           # 总收益
        'total_e2',                                                            # 总金额
        'day',                                                                 # 统计日期
        'month',                                                               # 
    ]