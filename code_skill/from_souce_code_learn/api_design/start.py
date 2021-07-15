# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     start
   Description :
   Author :       bing
   date：          2021/6/19
-------------------------------------------------
   Change Activity:
                   2021/6/19:
-------------------------------------------------
"""
__author__ = 'bing'
# 功能的插拔式设计。类似django中的settings
import notify
# 在这里面就可以全部执行
notify.send_all('快下课了')