#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PartnerRecordModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'partner_record'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = None  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                    # 自增ID
        'partner_uid',                                                           # 合伙人uid
        'order_id',                                                              # 订单id
        'open_amount_e2',                                                        # 订单金额
        'contract_amount_e2',                                                    # 合约价值
        'open_fee_e2',                                                           # 手续费
        'grants_fee_e2',                                                         # 赠金抵扣
        'phone',                                                                 # 订单创建人手机/邮箱
        'name',                                                                  # 订单创建人
        'rebate_e2',                                                             # 返佣金额
        'level',                                                                 # 提成层级
        'state',                                                                 # 数据状态[1:有效 0:删除]
        'is_send',                                                               # 是否发送返佣 [-1:已拒绝 0:未发送 1:已发送]
        'send_time',                                                             # 审核时间
        'create_time',                                                           # 创建时间
        'day',                                                                   # 订单日：20190828
        'month',                                                                 # 订单月：201908
        'child_uid',                                                             # 直接邀请人
        'type',                                                                  # 交易类型[1:合约 2:猜涨跌 3:现货 4:币本位用续]
        'currency_id',                                                           # token
    ]