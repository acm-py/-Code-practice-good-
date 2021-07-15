# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     动态生成变量
   Description :
   Author :       bing
   date：          2021/7/8
-------------------------------------------------
   Change Activity:
                   2021/7/8:
-------------------------------------------------
"""
__author__ = 'bing'
# 使用locals() ，它返回一个字典，记录着当前所有局部变量。
# 动态生成a1,a2,...a10个变量
ID = locals()
for i in range(1,11):
    ID['a' + str(i)] = 0 #设置默认值为0
# 但是有一个问题。
# locals() 用来创建局部变量，如果将上面的代码封装成函数，使用Locals()创建之后就只能在函数内部调用，
# 无法在全局调用
# 创建全局变量的是globals()
def dynamic_variable(n, variable_prefix='a'):
  for i in range(1,n+1):
    gd = globals()
    gd[variable_prefix+str(i)] = 0 # 新创建的n个变量，初始值都设置为0
