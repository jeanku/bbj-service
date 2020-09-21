#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class InMoneyModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'in_money'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                               # 自增ID
        'uid',                                                              # 用户ID
        'orderusdt_e2',                                                     # 准备入金金额(USDT)，单位：分
        'radio_e2',                                                         # 汇率 单位：分
        'orderrmb_e2',                                                      # 准备入金金额(人民币)，单位：分
        'outname',                                                          # 商家名称
        'outtype',                                                          # 商家收款类型 1支付宝 2银行卡 3.钱包
        'outaddr',                                                          # 商家收款账号
        'outbank',                                                          # 收款银行
        'intype',                                                           # 客户打款类型 1支付宝 2银行卡 3.钱包
        'inname',                                                           # 客户姓名
        'inaddr',                                                           # 客户打款账号
        'bank_flow_id',                                                     # 交易流水号
        'manager_name',                                                     # 管理员账号
        'approval_time',                                                    # 核销时间
        'confirm_time',                                                     # 确认付款
        'inrmb_e2',                                                         # 实际已入金金额(人民币)，单位：分
        'inusdt_e2',                                                        # 实际折算USDT，单位：分
        'state',                                                            # 订单状态 -99订单已被客户取消 1已创建,等待付款 2已付款,等待确认 3入金成功
        'remark',                                                           # 
        'create_time',                                                      # 创建时间
        'update_time',                                                      # 更新时间
        'status',                                                           # 状态：1正常，0删除
        'use_otc',                                                          # 1：otc，2:人工
        'app_id',                                                           # 
        'currency_id',                                                      # 
        'address',                                                          # 
        'tx_hx',                                                            # 
        'chain_type',                                                       # 
    ]