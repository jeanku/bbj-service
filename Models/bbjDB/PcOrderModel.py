#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class PcOrderModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'pc_order'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'order_id',                                                                 # 委托订单
        'uid',                                                                      # 用户ID
        'contract_id',                                                              # 交易对
        'side',                                                                     # 方向 1.开仓 2.平仓
        'amount',                                                                   # 保证金（委托时预收）
        'open_fee',                                                                 # 开仓手续费（预收）
        'close_fee',                                                                # 平仓手续费（预收）
        'amount_traded',                                                            # 按比例成交的预收的保证金
        'real_open_fee',                                                            # 真实收取的开仓手续费。多次成交需要多次累加
        'open_fee_returned',                                                        # 预收与实际开仓手续费之间差额的退款。多次有差额需要累加（不包含OpenFeeCancelled）
        'open_fee_cancelled',                                                       # 撤单导致的退回的开仓手续费
        'open_fee_returned_MP',                                                     # 市价委托时时退还给用户的开仓手续费
        'open_fee_traded',                                                          # 按比例成交的预收的开仓手续费
        'close_fee_traded',                                                         # 按成交比例预收的平仓手续费
        'close_fee_cancelled',                                                      # 撤单导致的退回的平仓手续费
        'close_fee_returned_MP',                                                    # 市价委托退回的平仓手续费
        'lever',                                                                    # 杠杆
        'bs_flag',                                                                  # 标志 1.看跌 2.看涨
        'price',                                                                    # 委托价
        'quantity',                                                                 # 委托量
        'quantity_MP',                                                              # 市价委托下，达到这个量就算完全成交
        'trading_quantity',                                                         # 正在挂单的量
        'order_type',                                                               # 委托类型 1.市价 2.限价
        'order_status',                                                             # 委托状态  1.正在申报 2.已申报未成交 3.部分成交 4.全部成交 5.部分撤单 6.全部撤单 7.撤单中 8.失效
        'maker_fee_ratio',                                                          # Maker 手续费
        'taker_fee_ratio',                                                          # Taker 手续费
        'user_order_id',                                                            # 持仓单ID
        'trade_currency',                                                           # 成交的本金（不含杠杆）
        'trade_quantity',                                                           # 成交量
        'trade_time',                                                               # 成交时间
        'cancel_quantity',                                                          # 撤单数量
        'pl',                                                                       # 本订单盈利
        'create_time',                                                              # 委托时间
        'update_time',                                                              # 更新时间
        'profit',                                                                   # 本单盈亏
        'amount_trade',                                                             # 保证金（根据实际成交金额计算出应付的保证金）
        'amount_cancelled',                                                         # 撤单时退回的保证金
        'amount_returned_MP',                                                       # 市价委托时退回的无法成交保证金
        'amount_difference',                                                        # 实际成交保证金与预收保证金之间的差额。只有在开仓或平仓全部完成，或撤单时更新。这个值是所有退还给用户的总值
        'new_quantity_MP',                                                          # 市价委托模式下，剩余未成交的部分新挂单量
        'new_price_MP',                                                             # 市价委托模式下，剩余未成交的部分新挂单的价
        'returned_amount',                                                          # 市价委托退回保证金
        'contract_type',                                                            # 仓位模式 1全仓 2逐仓
        'pre_sp_price',                                                             # 预设止盈价
        'pre_sl_price',                                                             # 预设止损价
        'pre_sp_ratio',                                                             # 预设止盈率
        'pre_sl_ratio',                                                             # 预设止损率
        'open_value',                                                               # 开仓总价值
        'close_value',                                                              # 平仓总价值
    ]