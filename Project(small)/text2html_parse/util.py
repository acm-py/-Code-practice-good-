# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     util
   Description :
   Author :       bing
   date：          2021/7/16
-------------------------------------------------
   Change Activity:
                   2021/7/16:
-------------------------------------------------
"""
__author__ = 'bing'

import collections
import io
"""
文本切割模块
处理 TXT 文本，创建返回文本块的生成器
"""
# 调用此函数时，file 参数一定是 IOWrapper 对象，
# IOWrapper 对象是迭代器对象

def lines(file: io.TextIOWrapper) -> collections.Iterator:
    """
    :param file: IOwrapper对象 -> iteror对象
    :return:
    """
    for line in file:
        yield line
    yield '\n'
# 同上一个函数 lines ，它也是个生成器函数
# 调用此函数时，file 参数一定是 IOWrapper 对象，IOWrapper 对象是迭代器对象
# 函数的返回值是生成器，生成器的每次迭代都会返回一个文本块
def blocks(file: io.TextIOWrapper) -> collections.Iterator:
    """
    生成器，将txt文件内容生成一个个单独的文本块，按空行分
    :param file:
    :return:
    """
    block = []
    for line in lines(file):
        # 如果不是空行
        if line.strip():
            block.append(line)
        # 如果是空行且block由内容
        # 这里可以看出 lines 生成器函数的作用了，如果最后一行不是空行
        # 那么最后一个文本块就不会作为 yield 的参数被生成器返回
        elif block:
            yield ''.join(block).strip()
        # 每次生成文本块后，要清空 block 列表
            block = []

