#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PcTradeOrderModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'pc_trade_order'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'order_id',                                                          # 订单ID
        'uid',                                                               # 用户ID
        'amount',                                                            # 开仓金额(本金) 。平仓时不减少。
        'fee',                                                               # 开仓手续费
        'contract_id',                                                       # 交易对ID、合约号
        'bs_flag',                                                           # 标志：1看跌 2看涨
        'open_price',                                                        # 建仓价
        'lever',                                                             # 建仓杠杆
        'sp_ratio',                                                          # 止盈比例 单位:百分之一
        'sp_price',                                                          # 止盈价
        'sl_ratio',                                                          # 止损比例 单位:百分之一
        'sl_price',                                                          # 止损价
        'force_price',                                                       # 强平价
        'close_type',                                                        # 平仓类型 1.挂单 2.持仓中 3.清仓
        'close_price',                                                       # 平仓价
        'close_time',                                                        # 平仓时间
        'pl',                                                                # 盈亏金额（未实现盈亏）
        'profit',                                                            # 盈亏金额（已实现盈亏）
        'remark',                                                            # 备注
        'update_time',                                                       # 更新时间
        'create_time',                                                       # 
        'order_type',                                                        # 订单类型 1:市价单，2：限价单
        'status',                                                            # 状态：1：正常2：取消
        'insurance_fund',                                                    # 保险基金（维持保证金）
        'fund_rate',                                                         # 保险基金率（维持保证金率）
        'waiver_rate',                                                       # 减免费率
        'is_append_bail',                                                    # 是否自动追加保证金：0:否  1:是
        'trading_qty',                                                       # 正在交易，但是未成交的合约数量
        'contract_qty',                                                      # 合约数量（已建仓）
        'closed_qty',                                                        # 合约数量（已平仓）
        'ava_qty',                                                           # 合约数量（可平仓）
        'freeze_qty',                                                        # 平仓成交前的冻结数量
        'open_value',                                                        # 开仓的总价值
        'close_value',                                                       # 平仓的总价值
        'funds_use',                                                         # 资金费用
        'funds_cost',                                                        # 余额不足扣除的资金费用
        'extra_margin',                                                      # 额外保证金
        'extra_cost',                                                        # 额外扣除保证金
        'close_fee',                                                         # 累计平仓手续费（预收）
        'real_close_fee',                                                    # 累计实收平仓手续费
        'contract_type',                                                     # 仓位类型 1全仓 2逐仓
    ]