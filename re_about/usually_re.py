# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     usually_re
   Description :
   Author :       bing
   date：          2021/7/8
-------------------------------------------------
   Change Activity:
                   2021/7/8:
-------------------------------------------------
"""
__author__ = 'bing'
# 匹配所有浮点数数字。
import re
pat_integ = '[1-9]+\d*'
pat_float0 = '0\.\d+[1-9]'
pat_float1 = '[1-9]\d*\.d+'
pat = 'r%s|%s|%s'%(pat_float0,pat_float1,pat_integ)
re.findall(pat, r)
['0.78', '3446.73', '0.91', '13642.95', '1.06', '2672.12', '3000']