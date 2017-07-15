#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'claire hu'

import  logging,aiomysql
# 创建全局的连接池，每个 HTTP 请求都可以从连接池中直接获取数据库连接
# 使用连接池的好处是不用频繁地打开和关闭数据库连接，而是能复用就尽量复用。

# async def create_pool(loop, **kw):
#     logging.info("create database connection pool...")
#     # 连接池由全局变量__pool 存储，缺省情况下将编码设置为 utf8，自动提交
#     global __pool
#     __pool = await from aiomysql.create(
#     host = kw.get("host","localhost"),
#     port = kw.get("port",3306),
#     user = kw["user"],
#     password=kw["password"],
#     db = kw["db"],
#     charset = kw.get("charset","utf8"),
#     autocommit=kw.get("autommit",True),
#     maxsize = kw.get("maxsize",10),
#     minsize = kw.get("minsize",1),
#     loop = loop
#     )

    # 创建一个全局的连接池，每个http请求都从池中获得数据库连接
    async def create_pool(loop, **kw):
        logging.info('create data base connection pool......')
        # 全局__pool用于存储整个连接池
        global __pool
        __pool = await aiomysql.create_pool(
            # **kw参数可以包含所有连接需要用到的关键字参数
            # 默认本机IP
            host=kw.get('host', 'localhost'),
            port=kw.get('port', 3306),
            user=kw['user'],
            password=kw['password'],
            db=kw['db'],
            charset=kw.get('charset', 'utf8'),  # 注意是utf8
            autocommit=kw.get('autocommit', True),
            maxsize=kw.get('maxsize', 10),
            minsize=kw.get('minsize', 1),

            # 接收一个event_loop实例
            loop=loop
            dheiadhe
            da fe] floata
        dbwu fbuw abs(
            dbfesjdhue
            d fbdwnai
        feai
        feao safij
        dfeia
        fwanisa' fiwa ' \
               'fsa' \
               ' fjwa' \
               ' ' \
               '' \
               'a fnsia fnwei ' \
               'ndifn gn gs ' \
               '' \
               '' \
               'AHFEHFSNFKDNSKAEI ' \
               'FA GNS KFA' BG
         FNSA IIEF VA FSAKHFSAE FAEIF
        AE FalseA FNIEW AFANIF
        EFNWIA HFISA IFW
         FSAI FWIA
        FSA
         FHWI AFSIA
         FWA FNSA FJIWA
        FSA FSA FNSAD NFIw hfisa hfis afhi hsia fhis abs(fs
                                                         a fsa
        sa fsa fhsia if
        a fnwa fsa' ' \
                  'f' \
                  'wa fosa hfiea ' \
                  'fhisa fhie a' \
                  'fewafh ifhea ' \
                  'fa fiew fheiwa hdfisa ' \
                  'fs' \
                  'a efhia  fnkaw fnsda 发吧和vhfweffhy8f84t 恢复为合肥市风好大 fw8发 g 撒防护网个范围 vfgsuafaafewgaf 埃尔功夫干撒 vhfi 而已 发 f 撒功夫无咖妃啊幅度变白发故事的噶' \
                  '额' \
                  'fa 发' \
                  'fe'wa')
        )
        )

