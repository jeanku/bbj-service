#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class TradeOrderModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'trade_order'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                    # 自增ID
        'uid',                                                                   # 用户ID
        'balance_e2',                                                            # 建仓前余额，单位：分
        'ex_balance_e2',                                                         # 下单前体验金余额
        'fee_e6',                                                                # 手续费率 单位:万分之一
        'open_amount_e2',                                                        # 建仓金额(本金) 单位:分
        'open_fee_e2',                                                           # 建仓手续费 单位:分
        'coupon_type',                                                           # 类型：1:U币 2:券 3.赠金 4.体验金
        'coupon_amount_e2',                                                      # 券面额(BTC数量) 单位:0.01BTC
        'coupon_nums',                                                           # 券数量
        'contract_id',                                                           # 行情价格ID
        'currency_id',                                                           # 币种
        'bs_flag',                                                               # 标志：1买跌 2买涨
        'open_price_e2',                                                         # 建仓价
        'open_new_price_id',                                                     # 建仓时的行情逐笔ID
        'open_time',                                                             # 建仓时间
        'lever',                                                                 # 建仓杠杆
        'sp_ratio_e2',                                                           # 止盈比例 单位:百分之一
        'sp_price_e2',                                                           # 止盈价
        'sl_ratio_e2',                                                           # 止损比例 单位:百分之一
        'sl_price_e2',                                                           # 止损价
        'force_price_e2',                                                        # 强平价
        'close_type',                                                            # 平仓类型 2.限价单3建仓 4手动平仓 5止盈平仓 6止损平仓 7爆仓平仓 8结算平仓9自动减仓
        'close_price_e2',                                                        # 平仓价
        'close_time',                                                            # 平仓时间
        'pl_e2',                                                                 # 盈亏金额
        'close_new_price_id',                                                    # 平仓时的行情逐笔ID
        'remark',                                                                # 备注
        'update_time',                                                           # 更新时间
        'create_time',                                                           # 
        'order_type',                                                            # 订单类型 1:市价单，2：限价单
        'status',                                                                # 状态：1：正常2：取消
        'show_status',                                                           # 平仓单是否显示在持仓列表1：显示2：不显示
        'grants_fee_e2',                                                         # 赠金抵扣手续费
        'grants_e2',                                                             # 下单前赠金余额
        'fee_waiver_e2',                                                         # 减免的手续费
        'insurance_fund_e2',                                                     # 保险基金
        'fund_rate_e6',                                                          # 保险基金率
        'waiver_rate_e6',                                                        # 减免费率
        'lever_e2',                                                              # 杠杆*100
        'is_append_bail',                                                        # 是否追加保证金：0:否  1:是
        'contract_e2',                                                           # 合约价值
        'funds_use_e2',                                                          # 资金费用 已经乘以100
        'funds_cost_e2',                                                         # 余额不足扣除的资金费用
        'amount_e2',                                                             # 
        'open_spread_up',                                                        # 开多点差
        'open_spread_down',                                                      # 开空点差
        'close_spread_up',                                                       # 平多点差
        'close_spread_down',                                                     # 平空点差
        'valid_time',                                                            # //有效时间
    ]