#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class OutMoneyModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'out_money'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                               # 自增ID
        'uid',                                                              # 用户ID
        'orderusdt_e2',                                                     # 出金金额(USDT)，单位：分，eos存的是e4
        'radio_e2',                                                         # 汇率 单位：分
        'fee_e2',                                                           # 手续费金额，单位：分
        'orderrmb_e2',                                                      # 出金金额(人民币)，单位：分
        'intype',                                                           # 客户收款类型 1支付宝 2银行卡 3.钱包
        'inname',                                                           # 客户姓名
        'inbank',                                                           # 客户收款银行
        'inaddr',                                                           # 客户收款账号
        'outname',                                                          # 商家名称
        'outtype',                                                          # 商家打款类型 1支付宝 2银行卡 3OTC
        'outaddr',                                                          # 商家打款账号
        'state',                                                            # 订单状态 99:成功 -1:审核通过 -2:提交审核 -3:审核不通过 -4:确认中 -99失败
        'bank_flow_id',                                                     # 交易流水号
        'manager_name',                                                     # 管理员账号
        'approval_time',                                                    # 核销时间
        'remark',                                                           # 备注
        'status',                                                           # 状态 1:正常 0:删除
        'create_time',                                                      # 创建时间
        'update_time',                                                      # 更新时间
        'currency_id',                                                      # 
        'app_id',                                                           # 
        'address',                                                          # 地址
        'chain_type',                                                       # 
    ]