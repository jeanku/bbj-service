#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class UserModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'user'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'uid',                                                                               # 用户ID
        'nickname',                                                                          # 昵称
        'login_pwd',                                                                         # 登录密码，密文
        'asset_pwd',                                                                         # 资产密码，密文
        'phone',                                                                             # 手机号，密文
        'email',                                                                             # 邮箱
        'create_time',                                                                       # 注册时间
        'login_time',                                                                        # 登录时间
        'register_ip',                                                                       # 注册ip
        'login_ip',                                                                          # 登录ip
        'type',                                                                              # 类型
        'status',                                                                            # 状态：0冻结，1正常
        'is_test',                                                                           # 是否为测试账号
        'account',                                                                           # 交易账号
        'kyc_status',                                                                        # 认证状态：0未认证，1.审核中 2.审核通过 3审核驳回
        'id_img1',                                                                           # 身份证正面
        'id_img2',                                                                           # 身份证反面
        'kyc_submit_time',                                                                   # 
        'kyc_pass_time',                                                                     # 
        'source',                                                                            # 
        'head_img',                                                                          # 头像图片URL
        'country',                                                                           # 国家标识
        'share_uid',                                                                         # 分享者uid
        'remark',                                                                            # 签名
        'update_time',                                                                       # 更新时间
        'name',                                                                              # 真实姓名
        'card_no',                                                                           # 身份号码
        'register_source',                                                                   # 注册来源
        'password_reset_token',                                                              # 
        'auth_key',                                                                          # 
        'otcname',                                                                           # 
        'partner_level',                                                                     # 合伙人等级 1：白银2：金牌  3：钻石
        'partner_update_time',                                                               # 合伙人等级修改时间
        'is_super_partner',                                                                  # 是否是超级合伙人 0：否 1：是
        'super_open_time',                                                                   # 超级合伙人开通时间
        'rebate_rate_e2',                                                                    # 合伙人等级的提成比例
        'system_rebate_rate_e2',                                                             # 后台设置的提成比例
        'is_rebate_second_open',                                                             # 是否开通二级返佣
        'is_rebate_third_open',                                                              # 是否开通三级返佣
        'is_show_child_partner_detail',                                                      # 是否允许查看子代理返佣详情
        'mykey_account',                                                                     # mykey账户
        'netease_token',                                                                     # 网易云信token
        'mykey_bind_time',                                                                   # mykey绑定时间
        'kyc_type',                                                                          # 身份认证类型 1:中国 2 其他地区
        'kyc_phone',                                                                         # 认证手机号
        'kyc_area',                                                                          # 认证地区
        'kyc_certificate',                                                                   # 证件类型
        'app_id',                                                                            # 合作平台ID：1BBJ，2mykey
        'chatroom_tag',                                                                      # 聊天室标签
        'coins_id',                                                                          # 现货id
        'mykey_id',                                                                          # mykey uuid
        'open_financial',                                                                    # 是否开启计息宝
        'open_order_race',                                                                   # 是否开启合约大赛 1是 2否
        'winning_tag',                                                                       # 打标高胜率用户 1是 0否
        'contract_type',                                                                     # 仓位模式 1全仓 2逐仓
        'is_open_reverse_contract',                                                          # 是否开启反向合约:0=>未开通;1=>开通
        'open_reverse_contract_time',                                                        # 开启反向合约的时间戳
        'open_reverse_contract_platform',                                                    # 开启的反向合约的平台:0:app端;1:PC端
        'guess_limit',                                                                       # 猜涨跌高胜率用户打标 0否 1是
        'guess_limit_rate_e2',                                                               # 猜涨跌高胜率用户下单失败率
        'guess_tag',                                                                         # 猜涨跌打标 1是 0否
        'contract_limit',                                                                    # 合约准入限制 0否 1是
        'contract_limit_rate_e2',                                                            # 合约下单失败率
        'language',                                                                          # 语言设置
        'agent_invite_code',                                                                 # 代理的注册邀请码
        'max_agent_propagenda',                                                              # 最大允许的推广数量
        'google_key',                                                                        # google验证私钥
        'bind_phone',                                                                        # 绑定的手机号
        'bind_email',                                                                        # 绑定的邮箱
        'phone_auth',                                                                        # 手机验证开启状态[0:关闭 1:开启 2:注册默认]
        'email_auth',                                                                        # 邮箱验证开启状态[0:关闭 1:开启 2:注册默认]
        'google_auth',                                                                       # google验证开启状态[0:关闭 1:开启]
    ]