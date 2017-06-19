#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'claire hu'

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from aiohttp import web

def index(request):
    # 打开 http://127.0.0.1:9000 调用，返回一个界面
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

async def init(loop):
    # 启动进入,得到 loop
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

# 创建一个名为 loop 的事件循环
loop = asyncio.get_event_loop()
# 调用 loop.run_until_complete 来运行 loop.create_server这个 coroutine 协程,加入运行事件
loop.run_until_complete(init(loop))
loop.run_forever()
