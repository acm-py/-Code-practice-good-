# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__
   Description :
   Author :       bing
   date：          2021/6/19
-------------------------------------------------
   Change Activity:
                   2021/6/19:
-------------------------------------------------
"""
__author__ = 'bing'
# 包方法
from code_skill.from_souce_code_learn.api_design import settings
import importlib


def send_all(content):
    for path_str in settings.NOTIFY_LIST:
        module_path, class_name = path_str.rsplit('.', maxsplit=1)
        # rspilt 从右边往左边切割 只切一次
        # 这个时候 module_name = notify.qq 、 notify.wechat、 notify.email
        # 通过importlib模块的import_module方法导入这些模块
        module = importlib.import_module(module_path)
        # 通过反射拿到类的名字
        cls = getattr(module, class_name)
        # 通过这些模块名，生成类实例
        obj = cls()
        # 利用鸭子类型调用send方法
        obj.send(content)
