#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""model类"""

__author__ = 'jemes'

from Models.BaseModel import BaseModel


class NewsModel(BaseModel):
    __database__ = 'bbj_db'  # 数据库名 对应.env中配置

    __tablename__ = 'news'  # 表名

    __create_time__ = 'create_time'  # 插入时间字段 如果该字段为None create_time则不会自动添加

    __update_time__ = 'update_time'  # 更新时间字段 如果该字段为None create_time则不会自动添加

    columns = [
        'id',                                                                    # 自增ID
        'title',                                                                 # 标题
        'content',                                                               # 内容
        'source',                                                                # 来源
        'type',                                                                  # 分类 1：新手必读 2：币 圈秘事 3：每日行情 4：推荐 5：快讯 6:常见问题 7聊天室 8.pc端常见问题
        'show_in_first_page',                                                    # 是否推荐到首页
        'create_time',                                                           # 创建时间
        'update_time',                                                           # 更新时间
        'status',                                                                # 状态：0：删除，1：正常
        'source_url',                                                            # 资讯来源
        'publishDate',                                                           # 文章发布时间
        'coverImgIds',                                                           # 封面图片地址
        'pv',                                                                    # 浏览量
        'bkb_id',                                                                # 币快报id
        'originName',                                                            # 来源
        'sortValue',                                                             # 排序字段
        'Interpretation',                                                        # 解读
        'see_more',                                                              # 看多
        'see_null',                                                              # 看空
        'highlight',                                                             # 是否高亮：1是0：否
        'articlesType',                                                          # 1：newsflashes快讯，2：ad广告
        'url',                                                                   # 七牛地址
        'has_video',                                                             # 是否有视频 1是 2否
    ]